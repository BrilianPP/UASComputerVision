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

The dataset used in this project is the **Mango Leaf Disease Dataset** sourced from [Kaggle](https://www.kaggle.com/datasets/aryashah2k/mango-leaf-disease-dataset). It contains **8 distinct classes of mango leaf images** stored in separate folders, with a total of **4,000 images**.

Here is the breakdown of images per class:

| No | Disease / Label         | Number of Images |
|----|--------------------------|------------------|
| 1  | Healthy                  | 500              |
| 2  | Powdery Mildew           | 500              |
| 3  | Anthracnose              | 500              |
| 4  | Bacterial Canker         | 500              |
| 5  | Cutting Weevil           | 500              |
| 6  | Die Back                 | 500              |
| 7  | Gall Midge               | 500              |
| 8  | Sooty Mould              | 500              |
|    | **Total**                | **4,000**        |

The data was split into training and testing sets with an 80:20 ratio. Each label was encoded and one-hot transformed for use in multi-class classification. Data augmentation was performed to increase dataset variability and improve model generalization.

---

## 🛠️ Tools & Technologies
- **Language:** Python  
- **Frameworks:** TensorFlow / Keras  
- **Method:** CNN  
- **Visualization:** OpenCV, Matplotlib  
- **Web Framework:** Flask  
- **Techniques:** Preprocessing, feature extraction, classification, bounding box detection  

---

## 🧠 Model Overview

The model built in this project is a **custom CNN architecture** designed from scratch without any pre-trained models. It consists of **three convolutional layers** with ReLU activation followed by **max pooling layers**, a **fully connected (dense) layer**, and an **output layer** with softmax activation for multi-class classification.

### 🧩 Model Layers:
- **Input Layer:** 256x256 RGB image  
- **Conv Layer 1:** 32 filters, 3x3 kernel, ReLU, MaxPooling  
- **Conv Layer 2:** 64 filters, 3x3 kernel, ReLU, MaxPooling  
- **Conv Layer 3:** 128 filters, 3x3 kernel, ReLU, MaxPooling  
- **Flatten Layer**  
- **Dense Layer:** 128 neurons, ReLU  
- **Dropout:** 0.5 (to prevent overfitting)  
- **Output Layer:** 8 neurons (for 8 classes), softmax  

### ⚙️ Training Configuration:
- **Optimizer:** Adam  
- **Loss Function:** Categorical Crossentropy  
- **Epochs:** 10  
- **Batch Size:** 32  
- **Callbacks Used:**
  - EarlyStopping: Monitors validation loss to avoid overfitting  
  - ReduceLROnPlateau: Adjusts learning rate if model stagnates  

  ![image](https://github.com/user-attachments/assets/cf8bf011-c464-4ee4-9084-4e4e4e26f9b1)

  ![image](https://github.com/user-attachments/assets/ac5e9aa4-1322-4641-b742-5dd23a935f81)


The model achieved a **validation accuracy of 92%** after training, demonstrating its effectiveness in classifying mango leaf diseases.

### Model Accuracy & Loss Graphs  
<p align="center">  
  <img src="Gambar/VisualisasiValAcc.png" width="450"/>  
  <img src="Gambar/VisualisasiValLoss.png" width="450"/>  
</p>  

### Confusion Matrix  
<p align="center">  
  <img src="Gambar/ConfMat.png" width="700"/>  
</p>  

---

## 💡 Disease Knowledge Integration

The system is enhanced by integrating disease treatment information for each identified disease. For example:

- **Anthracnose (Colletotrichum gloeosporioides):**  
  Recommended treatment includes the use of *Trichoderma* mixed with organic fertilizers and application of fungicides such as mancozeb, azoxystrobin, or carbendazim every 3–5 days during the flowering and fruit development stages.  
  *(Source: Ministry of Agriculture, 2016; Siregar & Nurmuharai, 2017)*

Similar handling descriptions are stored and displayed dynamically depending on the prediction results.

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

### Web Application Interface  
<p align="center">  
  <img src="Gambar/Home.png" width="450"/>  
  <img src="Gambar/Hasil.png" width="450"/>  
</p>  

---

## 📬 Contact  
- Email : mr.brilian871@gmail.com


