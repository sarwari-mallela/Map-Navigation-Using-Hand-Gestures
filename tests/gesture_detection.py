
import cv2 as cv
import json
from hand_tracking import HandTracker

def identify_gesture(img, lm_list):
    gestures = {}
    if len(lm_list) != 0:
        # Calculate the center of the hand
        x_center = sum(lm[1] for lm in lm_list) / len(lm_list)
        y_center = sum(lm[2] for lm in lm_list) / len(lm_list)

        # Define a threshold for movement to be considered a gesture
        movement_threshold = 50  # Adjusted threshold

        # Compare the center of the hand to the center of the image to identify gestures
        img_center_x, img_center_y = img.shape[1] // 2, img.shape[0] // 2

        # Draw a circle at the center of the hand for debugging
        cv.circle(img, (int(x_center), int(y_center)), 5, (0, 0, 255), cv.FILLED)

        if abs(y_center - img_center_y) < movement_threshold and abs(x_center - img_center_x) < movement_threshold:
            gestures['standby'] = True
        elif y_center < img_center_y - movement_threshold: gestures['pan_up'] = True
        elif y_center > img_center_y + movement_threshold: gestures['pan_down'] = True
        if x_center > img_center_x + movement_threshold: gestures['pan_left'] = True
        elif x_center < img_center_x - movement_threshold: gestures['pan_right'] = True

        # Calculate the distance between the thumb and the index finger
        thumb_index_distance = ((lm_list[4][1] - lm_list[8][1]) ** 2 + (lm_list[4][2] - lm_list[8][2]) ** 2) ** 0.5

        # Define a threshold for the thumb and index finger distance to be considered a gesture
        pinch_threshold = 50
        if thumb_index_distance < pinch_threshold:
            gestures['zoom_out'] = True
        elif abs(lm_list[4][1] - lm_list[8][1]) < pinch_threshold and abs(lm_list[4][2] - lm_list[8][2]) > pinch_threshold:
            gestures['zoom_in'] = True
            
        # Gesture priority system to only print out the most important gesture if multiple gestures are detected. 
        gesture_priority = ['zoom_in', 'zoom_out', 'pan_up', 'pan_down', 'pan_left', 'pan_right', 'standby']

        for gesture in gesture_priority:
            if gestures.get(gesture):
                return {gesture: True}
            
    return gestures

def gest_dect():
    print("Initialising camera and MediaPipe gestures...")
    try:
        cap = cv.VideoCapture(0)
        tracker = HandTracker()
        c = 0
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
                    print(f"gest {c}: {last_gest}")
                    # with open("../../gestures.json", "w") as file:
                    with open("./gestures.json", "w") as file:
                        json.dump(last_gest, file)
                    c+=1
                    prev_gest = last_gest

            cv.imshow("Image", img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()
    
    except Exception as e:
        print(f"Error in gesture detection: {e}")


gest_dect()