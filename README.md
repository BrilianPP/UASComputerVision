# 🍃 Mango Leaf Disease Detection 

## 👨‍🎓 Student Information
- **Name:** Brilian Purnama Putra  
- **Course/Institution:** Computer Vision / Politeknik Caltex Riau  

---

## 📌 Background
Indonesia has diverse vegetation, including the mango tree (*Mangifera indica*). While mangoes are tropical, they are widely cultivated, including in Indonesia. According to Indonesia’s Central Statistics Agency (BPS), mango production declined in 2023, partly due to leaf diseases.

Leaf diseases can be caused by insects, temperature fluctuations, bacteria, fungi, or viruses. Symptoms such as spots on leaves, flowers, fruits, and stems reduce yield and quality. Thus, early and automated detection is critical.

This project uses **Convolutional Neural Networks (CNNs)** to classify mango leaf diseases. The system is deployed via a web application that detects diseases, identifies the type, offers treatment suggestions, and highlights affected areas with bounding boxes and confidence scores.

---

## 🎯 Objectives
- Detect and classify mango leaf diseases using CNN  
- Display confidence scores for each prediction  
- Recommend treatment based on disease type  
- Show affected areas using yellow bounding boxes  
- Deploy the system in a user-friendly web interface  

---

## 🔍 Role of Computer Vision
- **Image Acquisition:** From dataset or user uploads  
- **Preprocessing:** Resizing, normalization, augmentation, color conversion  
- **Feature Extraction:** CNN learns patterns such as spots and textures  
- **Classification:** Identify disease or healthy leaf  
- **Bounding Box Visualization:** Highlights the affected area and confidence  
- **Treatment Recommendation:** Provided based on disease type  

---

## ✅ Benefits
- Assists farmers in quick and accurate disease detection  
- Offers early treatment solutions  
- Improves yield quality and reduces production losses  
- Reference for future plant disease classification systems  

---

## 🔒 Limitations
- Basic CNN architecture (no transfer learning)  
- Dataset limited to Kaggle  
- Only works with static images (not real-time input)  

---

## 📁 Dataset
- **Source:** [Kaggle - Mango Leaf Disease Dataset](https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset)

---

## 🛠️ Tools & Technologies
- **Language:** Python  
- **Frameworks:** TensorFlow / Keras  
- **Method:** CNN  
- **Visualization:** OpenCV, Matplotlib  
- **Web Framework:** Flask  
- **Techniques:** Preprocessing, feature extraction, classification, bounding box detection  

---

## 🚀 System Features
1. **Image Upload:** Upload leaf images via web UI  
2. **Disease Prediction:**  
   - Detect disease type automatically  
   - Show confidence score  
3. **Bounding Box Visualization:**  
   - Yellow box highlights infected area  
   - Label and confidence score displayed  
4. **Treatment Suggestion:**  
   - Example: "Anthracnose – Use copper-based fungicide"  
5. **Simple Web Interface:**  
   - Displays original image, prediction, bounding box, and suggested treatment  

---

## 📈 Project Progress
- ✅ Data preprocessing and augmentation  
- ✅ CNN model training (92% validation accuracy)  
- ✅ Bounding box implementation  
- ✅ Flask web application deployed  
- ✅ Full prediction output (classification, confidence, visualization, treatment)  
- ✅ **Project Status: 100% Complete**  

---

## 📊 Results

### Model Accuracy & Loss Graphs  
<p align="center">  
  <img src="Gambar/VisualisasiValAcc.png" width="450"/>  
  <img src="Gambar/VisualisasiValLoss.png" width="450"/>  
</p>  

### Confusion Matrix  
<p align="center">  
  <img src="Gambar/ConfMat.png" width="700"/>  
</p>  

### Web Application Interface  
<p align="center">  
  <img src="Gambar/Home.png" width="450"/>  
  <img src="Gambar/Hasil.png" width="450"/>  
</p>  

---

## 📬 Contact  
- Email : mr.brilian871@gmail.com


