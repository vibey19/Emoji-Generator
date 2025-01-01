😃 Facial Emotion Recognition using OpenCV and DeepFace

This project enables real-time facial emotion detection using the DeepFace library and OpenCV. It captures video from your webcam, detects faces, and identifies their emotions. Emotions are displayed as both text labels and emoji overlays on the video frames.

🛠️ Features

Real-time face detection: Utilizes Haar cascades for efficient face detection.

Emotion analysis: Leverages DeepFace for deep learning-based emotion recognition.

Emoji overlay: Displays corresponding emojis for detected emotions alongside text labels.

Interactive UI: A side-by-side view of emoji overlay and text-based emotion labeling.

🔗 Dependencies

Ensure you have the following libraries installed:

DeepFace: Deep learning library for facial analysis.

OpenCV: For video capture and image processing.

Install Dependencies

pip install -r requirements.txt

Or install individually:

pip install deepface
pip install tf_keras
pip install opencv-python

🔬 Getting Started

Clone the repository:

git clone https://github.com/manish-9245/Facial-Emotion-Recognition-using-OpenCV-and-Deepface.git
cd Facial-Emotion-Recognition-using-OpenCV-and-Deepface

Download Haar Cascade XML file:

Obtain haarcascade_frontalface_default.xml from the OpenCV GitHub repository.

Place it in the project directory.

Run the script:

python emotion_recognition.py

Output:

Webcam will open.

Detected emotions will be displayed as text and emojis.

Press q to exit.

🔎 How It Works

Face Detection:

Uses Haar cascades to identify faces in the video feed.

Emotion Prediction:

Processes detected faces using DeepFace to predict emotions.

Emoji Overlay:

Maps predicted emotions to emojis and overlays them on the frame.

Real-time Display:

Frames are updated continuously to show results in real time.

🔍 Code Overview

Core Features:

Libraries Used:

import cv2
from deepface import DeepFace

Emoji Integration:
Emojis are loaded as image files and resized to match face dimensions.

Overlay Function:
Adds emoji overlays with transparency using:

def overlay_image_alpha(img, img_overlay, x, y, alpha_mask): # Blend overlay within the determined region
...

Loop for Real-time Processing:

Captures video frames.

Detects faces and predicts emotions.

Displays results with text and emoji overlays.

📸 Example Output

Emoji and Text Display:

💡 Tips

Ensure adequate lighting for better face detection.

Test with different emotions for robust results.

Experiment with different Haar cascade files for improved performance.
