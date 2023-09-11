import cv2

## load an image using imread
img = cv2.imread("OpenCV Workshop, Aeromodelling Club\\Day 1\\1coffee.jpg")     # 2nd arg: 1= bgr, 0= grayscale, -1=unchanged

## print the shape of the loaded image
print(img.shape)

## resizing the image
img = cv2.resize(img,(640,480))

img = cv2.resize(img,(0,0),fx=0.1,fy=0.1)# 2nd arg: kitna dimension chahiye image ka.
                                            # (0,0) matlab jitne dimension ka hai utna rakho.

## displaying the image
cv2.imshow("coffee",img)
cv2.waitKey(0)      # 0= waits for infinite time