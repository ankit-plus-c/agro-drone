import cv2

## load an image using imread
img = cv2.imread("OpenCV Workshop, Aeromodelling Club\\Day 1\\1coffee.jpg")

## convert BGR to grayscale
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.resize(img2,(640,480))

## display the grayscale image
cv2.imshow("GrayScale",img2)
cv2.waitKey(0)