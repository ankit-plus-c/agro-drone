import cv2
import numpy as np

img = cv2.imread("Day 2\coffee.jpg")
img = cv2.resize(img, (640, 480))


# BLUR IMAGE
# Apply Gaussian Blur with kernel size (5, 5) - blur intensity, standard deviation - 0
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
# blurred_img = cv2.GaussianBlur(img, (15, 15), 0)



# CROPPING AN IMAGE
cropped_img = img[0:200, 440:640]
# cropped_img = img[100:200, 440:640]



# CANNY IMAGE
# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection with threshold values of 100 & 200
# last 2 arguments - threshold values, more difference -> less no. of edges
canny_img = cv2.Canny(gray_img, 100, 200)
# canny_img = cv2.Canny(gray_img, 100, 600)



# cv2.imshow("Blurred Image", blurred_img)
# cv2.imshow("Cropped Image", cropped_img)
cv2.imshow("Canny Image", canny_img)
cv2.waitKey(0)