
## 🤯 Emoji-Generator

This project enables real-time emotion detection using the `DeepFace` library and OpenCV. It captures video from your webcam, detects faces, and identifies emotions. Detected emotions are displayed as both text labels and emoji overlays on the video feed.


### 🚀 Features

- **Real-time Face Detection**: Utilizes Haar cascades for efficient face detection.
- **Emotion Analysis**: Uses `DeepFace` for deep learning-based emotion recognition.
- **Emoji Overlay**: Displays corresponding emojis for detected emotions.
- **Interactive UI**: Real-time side-by-side view of emoji overlay and text-based emotion labeling.


### 🔗 Dependencies

To run the project, ensure you have the following libraries installed:

- [DeepFace](https://github.com/serengil/deepface): For facial emotion recognition.
- [OpenCV](https://opencv.org/): For real-time video capture and processing.

#### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install deepface tf_keras opencv-python
```


### 🔬 Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vibey19/Emoji-Generator.git
   cd Emoji-Generator
   ```

2. **Download Haar Cascade XML file:**
   - Download `haarcascade_frontalface_default.xml` from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).
   - Place it in the project directory.

3. **Run the script:**

   ```bash
   python emotion_recognition.py
   ```

4. **Output:**
   - The webcam will open, showing real-time face detection.
   - Detected emotions will be displayed as text and emojis.
   - Press **`q`** to exit.


### 🔎 How It Works

- **Face Detection**: Uses Haar cascades to detect faces in the video feed.
- **Emotion Prediction**: Processes detected faces with `DeepFace` to predict emotions.
- **Emoji Overlay**: Maps emotions to emojis and overlays them on the video frames.


### 💡 Tips

- Ensure good lighting for accurate face detection.
- Test with different emotions for better results.
