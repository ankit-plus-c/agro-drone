import cv2

## video capturing

cap = cv2.VideoCapture("OpenCV Workshop, Aeromodelling Club\\Day 1\\1video.mp4")
## use video file
## cap = cv2.VideoCapture(0) # Use camera with index 0
## for external camera, you may use 1, 2, ...

while cap.isOpened():
    success, frame = cap.read()
    ## success - bool variable which ensures that the file is open or not
    ## frame - stores the file data

    if not success:
        break

    cv2.imshow("1video",frame)

    key = cv2.waitKey(1)    ## 1 - waits for one key press
    if key == ord('q'):     ## q - video keeps playing until key 'q' is pressed
        break