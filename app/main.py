import cv2

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

from gestures import detect_gesture

from actions import (
    volume_up,
    volume_down,
    take_screenshot
)

# Initialize hand tracking
mp_hands = hands.Hands()

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hands
    results = mp_hands.process(rgb_frame)

    gesture_text = ""

    # Detect hands
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            drawing_utils.draw_landmarks(
                frame,
                hand_landmarks,
                hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            # Detect gesture
            gesture_text = detect_gesture(landmarks)

            # Perform actions
            if gesture_text == "VOLUME UP":
                volume_up()

            elif gesture_text == "VOLUME DOWN":
                volume_down()

            elif gesture_text == "SCREENSHOT":

                success = take_screenshot()

                if success:
                    gesture_text = "SCREENSHOT TAKEN"

    # Display gesture text
    cv2.putText(
        frame,
        gesture_text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam
    cv2.imshow("Gesture Control AI", frame)

    # Quit with q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()