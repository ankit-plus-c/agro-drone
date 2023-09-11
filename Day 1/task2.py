import cv2

face_cascade = cv2.CascadeClassifier("1haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    x0 = 0
    y0 = 0
    w0 = 0
    h0 = 0
    nearest = 0
    for(x, y, w, h) in faces:
        area = w*h
        nearest = max(nearest, area)
        if nearest == area:
            x0 = x
            y0 = y
            w0 = w
            h0 = h

    cv2.rectangle(frame, (x0,y0), (x0+w0, y0+h0), (255,0,0), 2)

    cv2.imshow("video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()