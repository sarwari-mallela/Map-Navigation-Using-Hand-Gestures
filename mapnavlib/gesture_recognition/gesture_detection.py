
import cv2
from hand_tracking import HandTracker

def gesture_detection(img, lm_list):
    gestures = {}
    if len(lm_list) != 0:
        _, x_index, y_index = lm_list[8]  # Index Finger Tip
        _, x_thumb, y_thumb = lm_list[4]  # Thumb Tip

        # Pan Gestures
        if y_index < y_thumb - 100: gestures['pan_up'] = True
        elif y_index > y_thumb + 100: gestures['pan_down'] = True
        if x_index > x_thumb + 100: gestures['pan_right'] = True
        elif x_index < x_thumb - 100: gestures['pan_left'] = True

        # Zoom Gestures
        dist = ((x_index - x_thumb) ** 2 + (y_index - y_thumb) ** 2) ** 0.5
        if dist < 50: gestures['zoom_out'] = True
        elif dist > 200: gestures['zoom_in'] = True

    return gestures

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    while True:
        success, img = cap.read()
        img = tracker.find_hands(img)
        lm_list = tracker.find_position(img, draw=False)
        gestures = gesture_detection(img, lm_list)

        if (gestures != {}): print(list(gestures.keys())[0])

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
