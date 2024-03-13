
import cv2 as cv
# relative input:
from .gesture_detection import gest_dect
from .hand_tracking import HandTracker

def gesture():
    cap = cv.VideoCapture(0)  # Capture video from the first webcam
    tracker = HandTracker()
    
    while True:
        success, img = cap.read()
        if not success:
            break

        # Track hand and find landmark positions
        img = tracker.find_hands(img)
        lm_list = tracker.find_position(img, draw=False)
        
        # Detect gestures based on landmark positions
        if lm_list:
            gestures = gest_dect(img, lm_list)
            # Example action based on detected gestures (extend this part)
            if gestures:
                print("Detected gestures:", gestures)
                # Here, you would translate the detected gestures into actions,
                # such as controlling Google Maps.

        # Display the image
        cv.imshow("Gesture Controlled Google Maps", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()