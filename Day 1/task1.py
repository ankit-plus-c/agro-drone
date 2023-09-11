import cv2

cap = cv2.VideoCapture(0)
## use video file

while cap.isOpened():
    success, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not success:
        break

    cv2.imshow("video",gray)

    key = cv2.waitKey(1)    ## 1 - waits for one key press
    if key == ord('q'):     ## q - video keeps playing until key 'q' is pressed
        break