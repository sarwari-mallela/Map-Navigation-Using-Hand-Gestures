
import cv2 as cv
import json
from mapnavlib.gestures.hand_tracking import HandTracker

def identify_gesture(img, lm_list):
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

def gest_dect(shared_state):
    print("> Initialising camera and MediaPipe gestures...")
    try:
        cap = cv.VideoCapture(0)
        tracker = HandTracker()
        prev_gest = ""
        while 1:
            success, img = cap.read()
            if not success:
                raise Exception("Failed to read from camera")

            img = tracker.find_hands(img)
            lm_list = tracker.find_position(img, draw=False)
            gestures = identify_gesture(img, lm_list)

            # Write the gesture to a JSON file if gesture is different
            if gestures:
                last_gest = list(gestures.keys())[0]
                if prev_gest != last_gest:
                    print(f"gest: {last_gest}")
                    with open("./mapnavlib/gestures.json", "w") as file:
                        # Save gesture as an object with a 'gesture' property
                        json.dump({"gesture": last_gest}, file)
                    prev_gest = last_gest

            cv.imshow("Image", img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                shared_state.set_exit_flag(True)
                break

        cap.release()
        cv.destroyAllWindows()
    
    except Exception as e:
        print(f"Error in gesture detection: {e}")