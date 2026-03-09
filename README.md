Gesture Controlled Smart Assistant
Overview

The Gesture Controlled Smart Assistant is a system that allows users to control a computer using hand gestures captured through a webcam. Instead of using traditional input devices like a mouse or keyboard, users can perform gestures that are detected and interpreted by the system in real time.

The project uses computer vision and machine learning techniques to recognize gestures and map them to specific actions. This creates a more natural and contactless way of interacting with computers.

Features

Real-time hand gesture detection

Gesture-based computer control

Modular and scalable project structure

Lightweight and optimized for real-time performance

Easy integration with AI assistant modules

How It Works

The webcam captures live video input.

The system processes each frame using computer vision techniques.

A gesture recognition model detects and classifies the hand gesture.

The detected gesture is mapped to a predefined action.

The system executes the corresponding command.

Project Structure

app.py – Main application file
seed_gestures.py – Initializes or seeds gesture data
test_integration.py – Used for testing system integration
requirements.txt – Project dependencies

Folders:

database/ – Stores gesture data
models/ – Contains machine learning models
modules/ – Core functional modules of the system
utils/ – Helper and utility functions

Installation

Step 1: Clone the repository

git clone https://github.com/yourusername/gesture-controlled-assistant.git

Step 2: Navigate to the project folder

cd gesture-controlled-assistant

Step 3: Install the required dependencies

pip install -r requirements.txt

Usage

Run the main application using the following command:

python app.py

After running the program, the webcam will start and the system will begin detecting gestures in real time.

Technologies Used

Python
OpenCV
NumPy
Machine Learning
Computer Vision

Future Improvements

Voice and gesture hybrid assistant

Custom gesture training system

Improved deep learning gesture models

Web interface for gesture configuration

Integration with smart home or IoT devices

Author

Srikar
B V Raju Institute of Technology
