import cv2

# HSV IMAGE (Hue, Saturation, Value)
# hue - covers all the colors, 360 degrees (180 degrees in case of openCV i.e. 0 - 180)
# saturation - intensity of a color (0 - 255)
# brightness or value (0 - 255)

img = cv2.imread("Day 2\coffee.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("image", img2)
cv2.waitKey(0)