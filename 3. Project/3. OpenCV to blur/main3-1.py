#gray로 만든 사진에서 찾은후 다시 원본 color에 사각형 표시 하는것.
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #cv2.data저장소에서 얼굴을 찾는 xml알고리즘 파일
eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') #눈을 찾는 파일 찾아옴

ff = np.fromfile(r'40 Python works\3. Project\3. OpenCV to blur\face picture.jpg', np.uint8) #numpy를 이용해 한글경로 파일 불러옴. 원래는 한글경로 안됨
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) # OpenCV 라이브러리를 사용하여 이미지 파일을 디코딩하는 Python 코드 라인입니다. numpy파일을 디코딩하는것.
#numpy파일을 opencv2에서 작업할 수 있게 numpy배열을 반환하는 함수.
img = cv2.resize(img, (0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA) #첫 번째 인수 img는 크기를 조정해야 하는 입력 이미지입니다. 두 번째 인수(0, 0)는 출력 이미지의 크기를 지정하며, 이 경우 출력 이미지의 크기는 세 번째 인수와 네 번째 인수의 값을 기반으로 결정됩니다.
#1.0은 사진크기 그대로. 0, 0도 사이즈 그대로. 크기키우면 작아짐.
#다섯 번째 인수인 보간은 사용할 보간 방법을 지정합니다. INTER_AREA, 픽셀 영역 관계를 사용하여 이미지를 다시 샘플링하는 방법입니다. 이 방법은 다른 방법보다 앨리어싱 아티팩트가 적으면서 더 나은 결과를 생성하는 경향이 있으므로 다운샘플링(즉, 이미지의 크기를 줄이는 것)에 권장된다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #이미지를 한 색 공간에서 다른 색 공간으로 변환하는 기능입니다 BGR(Blue-Green-Red)

faces = face_cascade.detectMultiScale(gray, 1.2,5) #detectMultiScale함수 파라미터임.
#gray색에서 더쉽게 패턴을 찾아 얼굴을 탐지해서 gray, 1.2는 서로 다른 스케일의 얼굴을 검색하며, 스케일 팩터가 클수록 더 적은 수의 검출이 가능하다.
#5는 이 매개 변수는 후보 면 직사각형이 유효한 탐지로 간주되어야 하는 최소 이웃 수를 제어합니다. 이 매개 변수를 늘리면 탐지 수는 적지만 신뢰할 수 있는 탐지 수는 더 많아집니다. 
#함수는 검출된 면을 좌표로 나타내는 직사각형 배열을 반환합니다. 여기서 각 직사각형은 왼쪽 상단 모서리의 x와 y 좌표와 직사각형의 너비와 높이를 지정합니다.
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2) #시작점, 끝점, (255, 0, 0)은 컬러지정, 2는 직사각형 선의 두께
    roi_gray = gray[y:y+h, x:x+w] #새로운 관심 영역(roi), 얼굴 이미지 부분을 리턴함. gray부분에서 y~y+h, x~x+w까지 지정
    roi_color = img[y:y+h, x:x+w] #img부분에서 지정영역을 리턴함. 얼굴 부분을 리턴함.
    #차이는 gray는 흑백이란것, color는 원본 이미지, 흑백에서 더 잘 찾기떄문에 흑백영역도 지정해둔 것.
    eyes = eye_casecade.detectMultiScale(roi_gray) #영상내 눈을 감지하는데 사용
    for (ex, ey, ew, eh) in eyes: #검출된 눈의 좌표를 받음.
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0,255,0),2) #roi에 표시해 원본 이미지에 표시.

cv2.imshow('facefind', img) #얼굴과 눈 검출 결과를 화면에 보여준다.
cv2.waitKey(0) #cv2.waitKey(0)는 사용자가 아무 키나 누를 때까지 이미지 또는 비디오를 표시하며, 이때 함수는 누른 키의 ASCII 값을 반환합니다. 키를 누르지 않으면 기능은 계속해서 무한정 대기합니다.
cv2.destroyAllWindows() #위에서 아무키나 눌리면, 열린 모든 창을 닫는다.
