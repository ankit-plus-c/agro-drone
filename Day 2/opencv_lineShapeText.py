import cv2
import numpy as np

img = cv2.imread('Day 2\coffee.jpg')
img = cv2.resize(img, (640, 480))

image = cv2.namedWindow("image", cv2.WINDOW_NORMAL)
image = cv2.resizeWindow("image", 640, 480)
# cv2.waitKey(0)

cv2.line(img, (0,0), (640, 480), (255, 0, 0), 10)
cv2.line(img, (0,480), (640, 0), (255, 0, 0), 10)

cv2.rectangle(img, (255,255), (640, 480), (255, 255, 255), 8)   # coordinates - bottom left corner

cv2.circle(img, (320, 240), 240, (0, 0, 255), 5)

cv2.putText(img, "Areomodelling Club", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.5 , (0, 150, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)