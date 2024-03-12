
import cv2 as cv
import mediapipe as mp

# init MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

mp_draw = mp.solutions.drawing_utils

# open laptop's camera
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue

    # to improve performance, mark the frame as not writeable to pass by reference
    frame.flags.writeable = False
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame)

    # draw the hand annotations on the frame
    frame.flags.writeable = True
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # display frames with hand detection
    cv.imshow('Hand Detection', frame)

    # press 'q' to quit
    if cv.waitKey(0) == ord('q'):
        break

hands.close()
cap.release()