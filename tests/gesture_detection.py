import cv2 as cv
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

    return gestures

def gest_dect():
    cap = cv.VideoCapture(0)
    tracker = HandTracker()
    while True:
        success, img = cap.read()
        img = tracker.find_hands(img)
        lm_list = tracker.find_position(img, draw=False)
        gestures = identify_gesture(img, lm_list)
        print(gestures)
        # Calculate the middle point of the image
        img_center_x, img_center_y = img.shape[1] // 2, img.shape[0] // 2

        # Draw the middle point on the image for reference
        cv.circle(img, (img_center_x, img_center_y), 5, (0, 255, 0), cv.FILLED)

        # Display the image
        cv.imshow("Image", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
gest_dect()