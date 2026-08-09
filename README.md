<div align="center">

# 🏥 LUMIRA AI
### Multi-Modal Medical Imaging Diagnosis System

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>An AI-powered clinical decision support platform for multi-modal medical scan analysis.</b>
</p>

[🌐 Live Demo](#-live-demo--access) • [✨ Features](#-key-features) • [🛠️ Tech Stack](#️-tech-stack) • [🚀 Quick Start](#-quick-start)

---

</div>

## 📌 About Lumira AI

**Lumira AI** is an intelligent Deep Learning web application designed to aid medical diagnostic workflows. By unifying three specialized Computer Vision models into a single interface, it provides rapid automated analysis for Brain CT/MRI, Chest X-Rays, and Bone X-Rays.

---

## 🌐 Live Demo & Access

| Access Type | Link / Command |
| :--- | :--- |
| **🔗 Web App** | [Click Here to View Live App](https://your-app-name.streamlit.app) *(Update link after hosting)* |
| **💻 Local Host** | `streamlit run app.py` (Runs on `http://localhost:8501`) |

---

## ✨ Key Features

* 🧠 **Brain / Neuro Scan**: Identifies brain tumors and lesions from CT/MRI scans.
* 🫁 **Chest / Cardio Scan**: Detects cardiomegaly and cardiac abnormalities from Chest X-Rays.
* 🦴 **Bone / Ortho Scan**: Detects fractures in skeletal X-Ray images.
* 📊 **Confidence Metrics**: Displays automated probability and confidence scores for every inference.
* 🎨 **Interactive Interface**: Features a clean UI built with animated CSS gradients and Streamlit.

---

## 🛠️ Tech Stack

* **Core Engine**: Python 3.9+
* **Deep Learning Framework**: TensorFlow / Keras
* **Web Frontend**: Streamlit
* **Image Processing**: PIL (Pillow), NumPy

---

## 📂 Project Structure

```text
📁 Lumira_Medical_App/
│
├── 📄 app.py                  # Streamlit application logic & custom CSS UI
├── 🧠 lumira_neuro_model.h5   # Model for Brain Tumor detection
├── 🫁 lumira_cardio_model.h5  # Model for Cardiomegaly detection
├── 🦴 lumira_bone_model.h5    # Model for Bone Fracture detection
└── 📄 README.md               # Project documentation
```
## 🚀 Quick Start
1. Clone Repository
  ```
git clone [https://github.com/Sharika78/Lumira-AI.git](https://github.com/Sharika78/Lumira-AI.git)
cd Lumira-AI
```
2. Install Dependencies
 ```
   pip install tensorflow streamlit pillow numpy
```
3. Launch App
   ```
   streamlit run app.py
   ```
 ## 📜 License
This project is licensed under the MIT License - see below for details:
MIT License

Copyright (c) 2026 Lumira AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

## ⚠️ Disclaimer
Note: This application is an AI prototype developed exclusively for educational, research, and technical evaluation purposes. It is not intended for real clinical diagnosis or direct medical use.
   
     
