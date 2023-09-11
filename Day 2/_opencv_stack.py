import cv2
import numpy as np




def stackImages(scale, imgArray):
    rows = len(imgArray)
    columns = len(imgArray[0])
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    for x in range(0, rows):
        for y in range(0, columns):
            # current image is imgArray[x][y]
            if len(imgArray[x][y].shape == 2):
                imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imgArray[x][y] = cv2.resize(imgArray[x][y], (width, height))

    imgBlank = np.zeros((height, width*columns, 3), np.uint8)
    horizontal = [imgBlank]*rows

    for x in range(0, rows):
        horizontal[x] = np.stack(imgArray[x])

    ver = np.vstack(horizontal)
    ver = cv2.resize(ver, (0,0), None, scale, scale)
    return ver




img = cv2.imread("coffee.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.08, ([img, img, imgGray], [img, imgGray, img], [imgGray, img, img]))
cv2.imshow("images", imgStack)
cv2.waitKey(0)
