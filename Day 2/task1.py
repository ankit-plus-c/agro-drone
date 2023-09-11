import cv2

img = cv2.imread("Day 2\coffee.jpg")
img = cv2.resize(img, (640, 480))

cv2.line(img, (320, 240), (640, 240), (255, 255, 255), 10)
cv2.line(img, (320, 0), (320, 240), (0, 0, 255), 10)
cv2.line(img, (320, 0), (640, 240), (0, 255, 255), 10)

cv2.imshow("image", img)
cv2.waitKey(0)