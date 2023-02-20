import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 

ff = np.fromfile(r'40 Python works\3. Project\3. OpenCV to blur\face picture.jpg', np.uint8) 
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) 
img = cv2.resize(img, (0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

faces = face_cascade.detectMultiScale(gray, 1.2,5)
for (x,y,w,h) in faces:
    face_img = img[y:y+h, x:x+w]
    face_img = cv2.resize(face_img, dsize=(0,0), fx=0.05, fy=0.05) #모자이크 처리 얼마나할지 할 수 있음, 클수록 덜 모자이크함.
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = face_img

cv2.imshow('facefind', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

