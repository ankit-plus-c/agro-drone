import cv2
import numpy as np


def box_center(x, y, w, h):
    return (x + int(w/2)), (y + int(h/2))
detected = []


car_cascade = cv2.CascadeClassifier("cars.xml")

cap = cv2.VideoCapture("cctv.mp4")

totalCount = 0   # for counting the total number of detected cars

while True:
    success, frame = cap.read()

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # for detecting red cars
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    transformed = cv2.dilate(blur, np.ones((5, 5)))

    cars = car_cascade.detectMultiScale(transformed, 1.1, 4)

    count = 0      # for counting the number of detected cars in current frame

    lower_red = np.array([161, 155, 84])
    upper_red = np.array([179, 255, 255])

    for (x, y, w, h) in cars:
    
        if x >= 0 and x <= 480:     # for detecting cars only in the left lane
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 0, 255), 2)
            count += 1
            
            center = box_center(x, y, w, h)
            detected.append(center)
            for (x, y) in detected:
                if y >= 273 and y <= 293:
                    totalCount += 1
                detected.remove((x, y))
        
        mask = cv2.inRange(hsv_img, lower_red, upper_red)
        red_frame = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.putText(frame, str(count)+" left lane vehicles detected in current frame", (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.8 , (0, 150, 0), 1)
        print(str(count)+" left lane vehicles detected in current frame")

    cv2.putText(frame, "Detected Vehicle Count (if it gets detected", (0, 70), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 150, 0), 2)
    cv2.putText(frame, "in the center of the frame): "+str(totalCount), (0, 110), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 150, 0), 2)
    cv2.imshow("mask", red_frame)
    cv2.imshow("video", frame)

    if cv2.waitKey(33) == 27:
        break

print("Total no. of left lane cars detected:",totalCount)

cap.release()
cv2.destroyAllWindows()