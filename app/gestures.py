def detect_gesture(landmarks):

    gesture_text = ""

    # -------------------------
    # OPEN PALM DETECTION
    # -------------------------

    fingers = []

    # Index finger
    fingers.append(landmarks[8].y < landmarks[6].y)

    # Middle finger
    fingers.append(landmarks[12].y < landmarks[10].y)

    # Ring finger
    fingers.append(landmarks[16].y < landmarks[14].y)

    # Pinky finger
    fingers.append(landmarks[20].y < landmarks[18].y)

    # If all fingers up -> screenshot
    if all(fingers):

        return "SCREENSHOT"

    # -------------------------
    # THUMB DETECTION
    # -------------------------

    thumb_tip = landmarks[4]
    thumb_joint = landmarks[2]

    # Thumbs Up
    if thumb_tip.y < thumb_joint.y:

        return "VOLUME UP"

    # Thumbs Down
    elif thumb_tip.y > thumb_joint.y + 0.1:

        return "VOLUME DOWN"

    return gesture_text