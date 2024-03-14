
import cv2
from hand_tracking import HandTracker

def identify_gesture(img, lm_list):
    gestures = {}
    if len(lm_list) != 0:
        # Calculate the center of the hand
        x_center = sum(lm[1] for lm in lm_list) / len(lm_list)
        y_center = sum(lm[2] for lm in lm_list) / len(lm_list)

        # Set the threshold for the movement of the hand
        movement_threshold = 100  

        # Compare the center of the hand to the center of the image to identify gestures
        img_center_x, img_center_y = img.shape[1] // 2, img.shape[0] // 2

        # Draw a circle at the center of the hand for debugging
        cv2.circle(img, (int(x_center), int(y_center)), 5, (0, 0, 255), cv2.FILLED)

        if abs(y_center - img_center_y) < movement_threshold and abs(x_center - img_center_x) < movement_threshold:
            gestures['standby'] = True
        elif y_center < img_center_y - movement_threshold: 
            # Check if only the pointer and middle fingers are pointing up
            if lm_list[8][2] < lm_list[4][2] and lm_list[8][2] < lm_list[16][2] and lm_list[8][2] < lm_list[20][2] and lm_list[12][2] < lm_list[4][2] and lm_list[12][2] < lm_list[16][2] and lm_list[12][2] < lm_list[20][2]:
                gestures['pan_up'] = True
        elif y_center > img_center_y + movement_threshold: 
            gestures['pan_down'] = True
        if x_center > img_center_x + movement_threshold:
            # Check if only the pointer and middle fingers are pointing right
            if lm_list[8][1] > lm_list[4][1] and lm_list[8][1] > lm_list[16][1] and lm_list[8][1] > lm_list[20][1] and lm_list[12][1] > lm_list[4][1] and lm_list[12][1] > lm_list[16][1] and lm_list[12][1] > lm_list[20][1]:
                gestures['pan_left'] = True
        elif x_center < img_center_x - movement_threshold:
            # Check if only the pointer and middle fingers are pointing left
            if lm_list[8][1] < lm_list[4][1] and lm_list[8][1] < lm_list[16][1] and lm_list[8][1] < lm_list[20][1] and lm_list[12][1] < lm_list[4][1] and lm_list[12][1] < lm_list[16][1] and lm_list[12][1] < lm_list[20][1]:
                gestures['pan_right'] = True

    return gestures

def gest_dect():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    while True:
        success, img = cap.read()
        img = tracker.find_hands(img)
        lm_list = tracker.find_position(img, draw=False)
        gestures = identify_gesture(img, lm_list)

        # Calculate the middle point of the image
        img_center_x, img_center_y = img.shape[1] // 2, img.shape[0] // 2

        # Draw the middle point on the image for reference
        cv2.circle(img, (img_center_x, img_center_y), 5, (0, 255, 0), cv2.FILLED)

        # Display the image
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
