project name - Gesture Control AI
A real-time computer vision system that uses hand gestures to control computer actions using a webcam.

Features
Real-time hand tracking using computer vision
Gesture recognition (open hand, thumbs up , thumbs down, etc.)
Trigger system actions using gestures
Modular architecture (clean separation of logic)
Works in real-time via webcam

How It Works
Captures live video from webcam
Detects hand landmarks
Interprets finger positions as gestures
Maps gestures to system actions
Executes actions instantly

Tech Stack
Python
OpenCV
MediaPipe
NumPy

 Installation
git clone https://github.com/your-username/gesture-control-ai.git
cd gesture-control-ai
pip install -r requirements.txt
▶ run the Project
python app/main.py

 Gestures

palm detected = screenshot 
thumbs up = volume up 
thumbs down = volume down 

 Future Improvements
Add more gestures
Improve accuracy with ML model
Add GUI overlay
System-wide mouse control

 License
This project is not licensed for reuse, modification, or redistribution without permission.

Author
brinda hingu
