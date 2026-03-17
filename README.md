# 🤟 Sign Language Recognition System

A real-time Sign Language Recognition system built using **Python, OpenCV, and MediaPipe** that detects hand gestures through a webcam and predicts corresponding alphabets using a Machine Learning model.

<img width="1324" height="820" alt="Screenshot 2026-03-17 222547" src="https://github.com/user-attachments/assets/6d721881-d829-45fb-98b6-38bca38e1584" />

---

## 🚀 Features

* 📸 Real-time hand tracking using webcam
* ✋ Hand landmark detection using MediaPipe
* 🧠 Machine Learning model (Random Forest) for classification
* 🔤 Predicts sign language alphabets (A, B, L, etc.)
* 📂 Custom dataset creation and training pipeline

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📁 Project Structure

```
sign-language-project/
│── data/                  # Collected images for each class  
│── collect_image.py       # Script to collect dataset  
│── create_dataset.py      # Extract hand landmarks  
│── train_classifier.py    # Train ML model  
│── webcam_classifier.py # Real-time prediction  
│── model.p                # Trained model  
│── data.pickle            # Processed dataset  
```

---

## ⚙️ How It Works

1. **Data Collection**
   Capture images of hand gestures using webcam.

2. **Data Processing**
   Extract hand landmarks using MediaPipe.

3. **Model Training**
   Train a Random Forest classifier on extracted features.

4. **Real-Time Prediction**
   Use webcam to detect hand signs and display predicted alphabet.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```
pip install opencv-python mediapipe scikit-learn numpy
```

### 2️⃣ Collect Data

```
python collect_image.py
```

### 3️⃣ Create Dataset

```
python create_dataset.py
```

### 4️⃣ Train Model

```
python train_classifier.py
```

### 5️⃣ Run Prediction

```
python webcam_classifier.py
```

---

## 🎯 Future Improvements

* Add full alphabet support (A–Z)
* Improve model accuracy using deep learning
* Add word/sentence recognition
---

