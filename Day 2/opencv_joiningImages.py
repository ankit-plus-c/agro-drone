import cv2
import numpy as np

# HORIZONTAL STACK
# image ~ array
img = cv2.imread("Day 2\coffee.jpg")
img = cv2.resize(img, (640, 480))   # dimension = 3
horizontal = np.hstack((img, img))
print(img.shape)


# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # dimension = 2
# print(img2.shape)

# horizontal = np.hstack((img, img2)) # won't work as it can't stack 2 arrays of different dimensions


# Trick !!
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # dimension = 2
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)    # dimension = 3 again

horizontal = np.hstack((img, img2))



# VERTICAL STACK
img = cv2.imread("Day 2\coffee.jpg")
img = cv2.resize(img, (320, 240))
vertical = np.vstack((img, img))



cv2.imshow("horizontal", horizontal)
cv2.imshow("vertical", vertical)
cv2.waitKey(0)