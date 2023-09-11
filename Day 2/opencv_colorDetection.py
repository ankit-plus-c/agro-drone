import cv2
import numpy as np

def empty(a):
    pass

img = cv2.imread("Day 2\color.jpg")
img = cv2.resize(img, (480, 280))

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 480, 280)
cv2.createTrackbar("h_min", "Trackbars", 0, 179, empty)     # hue minimum, 3rd argument = initial position
cv2.createTrackbar("h_max", "Trackbars", 179, 179, empty)   # hue maximum
cv2.createTrackbar("s_min", "Trackbars", 0, 255, empty)     # saturation minimum
cv2.createTrackbar("s_max", "Trackbars", 255, 255, empty)   # saturation maximum
cv2.createTrackbar("v_min", "Trackbars", 0, 255, empty)     # value minimum
cv2.createTrackbar("v_max", "Trackbars", 255, 255, empty)   # value maximum
cv2.imshow("Image", img)
cv2.imshow("HSV Image", hsv_img)


while True:
    hue_min = cv2.getTrackbarPos("h_min", "Trackbars")
    hue_max = cv2.getTrackbarPos("h_max", "Trackbars")
    sat_min = cv2.getTrackbarPos("s_min", "Trackbars")
    sat_max = cv2.getTrackbarPos("s_max", "Trackbars")
    val_min = cv2.getTrackbarPos("v_min", "Trackbars")
    val_max = cv2.getTrackbarPos("v_max", "Trackbars")
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(hsv_img, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    cv2.waitKey(1)