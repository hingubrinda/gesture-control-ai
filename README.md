# ✋ GESTURE CONTROL AI  
### Real-time Hand Gesture Recognition System for Computer Control

---

## 🚀 Overview

Gesture Control AI is a real-time computer vision project that enables hands-free interaction with a computer using hand gestures detected via webcam.

It uses **MediaPipe** for hand landmark detection and **OpenCV** for video processing to interpret gestures and map them to system actions.

---

## ⚡ Key Features

- Real-time webcam-based hand tracking  
- 21-point hand landmark detection  
- Gesture recognition system  
- System action mapping (click, scroll, idle, etc.)  
- Lightweight and runs in real-time  
- Modular and clean architecture  

---

## 🎥 Demo

👉 Watch full working demo:  
[https://drive.google.com/file/d/1f0W-ab4nvRO-LnbHNlcmk0KUbNLAtoge/view?usp=sharing](https://drive.google.com/file/d/1f0W-ab4nvRO-LnbHNlcmk0KUbNLAtoge/view?usp=sharing)

---

## 🧠 How It Works

Webcam → Hand Detection → Landmark Tracking → Gesture Recognition → Action Execution

1. Captures live video using webcam  
2. Detects hand using MediaPipe  
3. Extracts finger landmark positions  
4. Identifies gesture based on finger configuration  
5. Triggers mapped system action  

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- PyAutoGUI  



▶️ Run Project
python app/main.py
Make sure your webcam is enabled.

✋ Supported Gestures
Gesture	Action
open palm = screenshot 
thumbs up = volume up 
thumbs down = volume down 

🔮 Future Improvements
Add more gesture types
Improve accuracy using ML model
Add GUI overlay system
Full mouse & keyboard control
Gesture customization panel

📌 Highlights
Real-time processing
Computer vision based control
Works completely offline
Lightweight and efficient
Beginner-friendly architecture

📜 License
This project is not licensed for reuse or redistribution without permission.

👨‍💻 Author
Brinda Hingu
GitHub: https://github.com/hingubrinda

