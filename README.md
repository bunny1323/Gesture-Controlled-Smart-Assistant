Gesture Controlled Smart Assistant

An AI-powered system that allows users to control their computer using hand gestures captured through a webcam. The assistant uses computer vision and machine learning techniques to detect gestures in real time and map them to system actions.

This project demonstrates how natural human interaction can replace traditional input devices such as a mouse or keyboard.

Demo

Example workflow:

Camera captures hand gestures

Gesture detection model processes frames

Recognized gesture triggers system command

Assistant performs the action

Features

Real-time hand gesture detection

Contactless computer control

Modular architecture for easy upgrades

Gesture dataset initialization support

Integration testing included

Lightweight and optimized for real-time performance

System Architecture
Camera Input
     │
     ▼
Frame Processing (OpenCV)
     │
     ▼
Gesture Recognition Model
     │
     ▼
Gesture Classification
     │
     ▼
Action Mapping Module
     │
     ▼
System Command Execution


Project Structure
gesture-controlled-assistant
│
├── app.py
├── seed_gestures.py
├── test_integration.py
├── requirements.txt
├── README.md
│
├── database/
│   └── Gesture dataset storage
│
├── models/
│   └── Gesture recognition models
│
├── modules/
│   └── Core system modules
│
└── utils/
    └── Helper and utility functions

    
Installation
Clone the repository:

git clone https://github.com/yourusername/gesture-controlled-assistant.git

Navigate to the project folder:
cd gesture-controlled-assistant

Install dependencies:

pip install -r requirements.txt
Usage

Run the main application:

python app.py

The system will activate the webcam and start detecting gestures in real time.

Technologies Used

Python

OpenCV

NumPy

Machine Learning

Computer Vision

Example Gesture Actions
Gesture	Action
Open Palm	Start Assistant
Closed Fist	Stop Assistant
Swipe Left	Previous Action
Swipe Right	Next Action
Two Fingers	Select Command

(You can modify these gestures in the dataset.)

Future Improvements

Voice + gesture hybrid assistant

Custom gesture training interface

Deep learning-based gesture recognition

Web dashboard for configuration

IoT device control integration

Contribution

Contributions are welcome.

Fork the repository

Create a new branch

Commit your changes

Submit a pull request

License

This project is open-source and available under the MIT License.

Author

Developed by Srikar
B V Raju Institute of Technology

✅ After adding this:

git add README.md
git commit -m "Added professional README"
git push
