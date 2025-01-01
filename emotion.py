import cv2
from deepface import DeepFace

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video
cap = cv2.VideoCapture(0)

# Load emoji images
emoji_images = {
    "angry": cv2.imread("./emojis/angry.png", cv2.IMREAD_UNCHANGED),
    "disgust": cv2.imread("./emojis/disgust.png", cv2.IMREAD_UNCHANGED),
    "fear": cv2.imread("./emojis/fear.png", cv2.IMREAD_UNCHANGED),
    "happy": cv2.imread("./emojis/happy.png", cv2.IMREAD_UNCHANGED),
    "sad": cv2.imread("./emojis/sad.png", cv2.IMREAD_UNCHANGED),
    "surprise": cv2.imread("./emojis/surprise.png", cv2.IMREAD_UNCHANGED),
    "neutral": cv2.imread("./emojis/neutral.png", cv2.IMREAD_UNCHANGED)
}


def overlay_image_alpha(img, img_overlay, x, y, alpha_mask):
    """Overlay `img_overlay` onto `img` at (x, y) with alpha channel from `alpha_mask`."""
    h, w = img_overlay.shape[:2]

    # Image overlay region
    y1, y2 = max(0, y), min(img.shape[0], y + h)
    x1, x2 = max(0, x), min(img.shape[1], x + w)

    y1o, y2o = max(0, -y), min(h, img.shape[0] - y)
    x1o, x2o = max(0, -x), min(w, img.shape[1] - x)

    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    # Blend overlay within the determined region
    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o, None] / 255.0

    img_crop[:] = (1.0 - alpha) * img_crop + alpha * img_overlay_crop


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Create a copy for emoji overlay
    frame_with_emoji = frame.copy()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(
            face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        emoji_img = emoji_images.get(emotion, None)

        # For emoji overlay
        if emoji_img is not None:
            # Resize emoji to fit the face bounding box
            emoji_resized = cv2.resize(
                emoji_img, (w, h), interpolation=cv2.INTER_AREA)

            # Overlay the emoji on the frame
            overlay_image_alpha(
                frame_with_emoji, emoji_resized[:, :, :3], x, y, emoji_resized[:, :, 3])

        # For text overlay
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Concatenate the two views side by side
    side_by_side = cv2.hconcat([frame_with_emoji, frame])

    # Display the side-by-side result
    cv2.imshow('Real-time Emotion Detection (Emoji | Text)', side_by_side)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
