import cv2

img = cv2.imread("Day 2\color.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 155, 255, 0)  # gray scale image used so that it detects the contours easily
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
# cv2.drawContours(img, contours, 1, (0, 255, 0), 2)  # for a single contour
print("Number of contours: ", len(contours))    # for the number of detected contours

cv2.drawContours(gray, contours, -1, (0, 255, 255), 3)

cv2.imshow("image", img)
cv2.imshow("gray image", gray)

cv2.waitKey(0)