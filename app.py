from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load the model and class labels
try:
    model = load_model('modelfix2.h5')
    disease_info = {
        0: {
            "name": "Healthy",
            "cause": "",
            "treatment": "Pohon mangga Anda sehat! Lanjutkan perawatan rutin untuk menjaga kesehatannya."
        },
        1: {
            "name": "Powdery Mildew",
            "cause": "Penyebab: Jamur Oidium mangiferae / Jamur Erysiphe cichoracearum",
            "treatment": "Penanganan penyakit Empung Tepung (Powdery Mildew) pada mangga dapat menggunakan fungisida yang mengandung Bacillus licheniformis yang mengurangi infeksi jamur. Selain itu juga dapat menggunakan fungisida dengan kandungan garam monopotassium, minyak tanah hidrodesulfurisasi, pelarut minyak bumi alifatik, mancozeb dan myclobutanil. Untuk efek optimal, perlakuan harus dimulai sebelum berbunga atau pada tahap berbunga sangat awal dan direkomendasikan untuk diaplikasikan secara berkala selama 7-14 hari. (Sumber: Plantix.net; Siregar & Nurmuharai, 2017)"
        },
        2: {
            "name": "Anthracnose",
            "cause": "Penyebab: Jamur Colletotrichum gloeosporiodes",
            "treatment": "Pengendalian penyakit Antraknosa (Colletotrichum gloeosporioides) dengan ditambahkan pemakaian trichoderma dicampur dengan pupuk kandang. Penyemprotan dengan menggunakan fungisida kombinasi mancozeb, dicotophos, propineb, azoksistrobin, dipenokonazol, karbenazim, tiram dalam selang waktu 3-5 hari sekali dari saat pembentukan tunas bunga hingga fase pemasakan buah. (Sumber: Dinas Pertanian Tanaman Pangan, 2016; Siregar & Nurmuharai, 2017)"
        },
        3: {
            "name": "Bacterial Canker",
            "cause": "Penyebab: Bakteri Pseudomonas syringae",
            "treatment": "Penanganan penyakit Bakteri Hama (Bacterial Canker) pada mangga dapat diatasi dengan penggunaan bakterisida organik yang mengandung senyawa tembaga atau campuran Bordeaux. (Sumber: Plantix.net)"
        },
        4: {
            "name": "Cutting Weevil",
            "cause": "Penyebab: Kumbang pemotong (Curculionidae)",
            "treatment": "Penanganan Cutting Weevil pada mangga dapat menggunakan insektisida seperti deltametrin dan fenvalerat untuk melindungi tunas muda dari serangan kumbang. Saat daun muda masih kecil, sebaiknya semprotkan pestisida untuk melindungi daun dan tunas (Sumber: Plantix.net)"
        },
        5: {
            "name": "Die Back",
            "cause": "Penyebab: Jamur Botryodiplodia rhodina / Jamur Lasiodiplodia theobromae",
            "treatment": "Penanganan penyakit Mati Pucuk (Die Back) pada mangga dapat diatasi dengan menyingkirkan dan memusnahkan bagian pohon yang terinfeksi sesegera mungkin beserta cabang sehat di sekitarnya untuk memastikan pemberantasan patogen secara lengkap. Selanjutnya dapat dilakukan dengan memberikan tembaga oksiklorida dengan konsentrasi 0,3% pada luka tanaman atau memberikan campuran Bordeaux dua kali setahun untuk mengurangi tingkat infeksi (Sumber: Plantix.net)"
        },
        6: {
            "name": "Gall Midge",
            "cause": "Penyebab: Lalat Jatrophobia brasiliensis / Serangga Procontarinia matteiana / Tungau Eriophyidae",
            "treatment": "Penanganan penyakit Gall Midge pada mangga dapat dilakukan dengan membuang bagian pohon yang terjangkit jika serangan parah. Semprotan pencegahan dengan insektisida/mitisida yang mengandung abamektin atau bifentrin dapat melindungi pohon dari serangan tungau (Sumber: Plantix.net)"
        },
        7: {
            "name": "Sooty Mould",
            "cause": "Penyebab: Jamur Capmodium mangiferum / Virus Meliola mangifera",
            "treatment": "Penanganan penyakit Jamur Hitam (Sooty Mould) pada mangga dapat dilakukan dengan memberantas serangga yang menghasilkan cairan manis memakai insektisida atau tepung belerang. Selain itu, juga dapat menggunakan formulasi minyak nimba yang menangkal hama dan pertumbuhan fungi itu sendiri serta pemakaian insektisida sintetik dari keluarga organofosfat seperti malathion untuk mencegah serangga (Sumber: blog.tokotanaman.com; plantix.net)"
        }
    }
except Exception as e:
    print(f"Error loading model: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return render_template('prediksi.html', error="No image file uploaded")

        file = request.files['image']

        if file.filename == '':
            return render_template('prediksi.html', error="No selected file")

        # Validasi ekstensi
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if not file.filename.lower().endswith(tuple(allowed_extensions)):
            return render_template('prediksi.html', error="Invalid file type. Allowed types: png, jpg, jpeg")

        # Load dan preprocess gambar
        from io import BytesIO
        import cv2
        import matplotlib.pyplot as plt

        img_pil = Image.open(file).convert("RGB")
        img_resized = img_pil.resize((256, 256))
        img_array = np.array(img_resized) / 255.0
        img_input = np.expand_dims(img_array, axis=0)

        # Prediksi
        predictions = model.predict(img_input)
        class_index = np.argmax(predictions)
        confidence = predictions[0][class_index]

        # Informasi penyakit
        disease_data = disease_info[class_index]

        # Anotasi gambar dengan bounding box dan label
        img_cv = np.array(img_pil)[:, :, ::-1].copy()  # Convert to BGR
        h, w, _ = img_cv.shape

        # Hitung margin bounding box proporsional
        margin_w = int(w * 0.05)
        margin_h = int(h * 0.05)
        top_left = (margin_w, margin_h)
        bottom_right = (w - margin_w, h - margin_h)

        # Buat overlay gelap di seluruh gambar
        overlay = img_cv.copy()
        dark_overlay = np.zeros_like(img_cv, dtype=np.uint8)
        dark_overlay[:] = (0, 0, 0)  # Hitam

        # Copy area dalam bounding box dari gambar asli
        bright_area = img_cv[margin_h:h - margin_h, margin_w:w - margin_w].copy()
        dark_overlay[margin_h:h - margin_h, margin_w:w - margin_w] = bright_area

        # Gabungkan overlay dengan alpha blending
        alpha = 0.5
        img_cv = cv2.addWeighted(img_cv, alpha, dark_overlay, 1 - alpha, 0)

        # Gambar garis bounding box kuning
        cv2.rectangle(img_cv, top_left, bottom_right, (0, 255, 255), 2)

        # Teks label di atas bounding box
        label_text = f"{disease_data['name']} ({confidence * 100:.1f}%)"
        font_scale = h / 700.0
        font_thickness = max(2, int(h / 250))
        text_color = (255, 255, 255)  # Putih

        # Ukuran dan posisi teks
        (text_w, text_h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
        text_x = top_left[0] + 5
        text_y = top_left[1] - 10 if top_left[1] - 10 > text_h else top_left[1] + text_h + 10

        # Background gelap semi-transparan untuk teks
        cv2.rectangle(img_cv, (text_x - 5, text_y - text_h - 5), (text_x + text_w + 5, text_y + 5), (0, 0, 0), -1)
        cv2.putText(img_cv, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

        # Simpan hasil gambar ke folder static
        result_image_path = os.path.join('static', 'predicted_image.jpg')
        cv2.imwrite(result_image_path, img_cv)

        # Kirim data ke template
        result = {
            'disease': disease_data['name'],
            'confidence': round(float(confidence) * 100, 2),
            'cause': disease_data['cause'],
            'treatment': disease_data['treatment'],
            'image_path': result_image_path
        }

        return render_template('prediksi.html', result=result)

    except Exception as e:
        return render_template('prediksi.html', error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)
