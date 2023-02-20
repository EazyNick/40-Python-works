#PYQT를 사용한 계산기 GUI프로그램 만들기
#PYQT의 GUI를 만드는 라이브러리를 활용해 윈도우의 계산기와 비슷하게 만들어보자. 디자인 가능!
#터미널에 designer을 입력
#Main Window 선택
#오브젝트 내임을 써서 실제 코드에서 가져다 쓸 수 있다.

#2. Qt Designer로 계산기 Widget 만들기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# [계산기.ui] 불러오기
ui_path = r"40 Python works\3. Project\6. Calculator GUI Program Using PYQT\계산기.ui"  #경로
form_class = uic.loadUiType(ui_path)[0] #ui타입 로드
# WindowClass 생성/ form_class로부터 상속받은 자식 클래스/ form_class는 [계산기.ui]
class WindowClass(QMainWindow, form_class):#QMainWindow는 PyQt 라이브러리에서 미리 정의된 클래스로 메인 응용 프로그램 창을 제공
    def __init__(self):
        super().__init__() # 다른 클래스의 속성 및 메소드를 자동으로 불러와 해당 클래스에서도 사용가능하게 해줌
#부모의 init속성을 가져온다는 뜻.
        self.setupUi(self) #UI설치

if __name__ == "__main__":#if __name_(현재 모듈이름을 담고있는 내장변수) == "_main_:" 조건은 스크립트가 메인 프로그램으로 실행되고 있는지 또는 모듈로 가져오고 있는지 확인하는 파이썬의 일반적인 패턴
#모듈을 직접 실행시켰을 때만 실행되도록 하는 코드를 작성하기 위해서 사용
#직접 main6-1.py를 터미널에서 직접 실행하면 __name__변수에 __main__이라는 값이 할당된다.
# GUI 불러오기
    app = QApplication(sys.argv)# QApplication 클래스는 주 응용 프로그램 개체를 만드는 데 사용됩니다. sys.argv는 스크립트에 전달된 명령 인수를 포함하는 Python의 목록입니다. QA 애플리케이션에 전달함으로써 애플리케이션에 전달된 명령 인수를 처리할 수 있습니다.
    myWindow = WindowClass()
    myWindow.show() #show() 메서드는 화면에 창을 표시합니다.
    app.exec_() #exec_() 메서드는 메인 응용 프로그램의 이벤트 루프를 시작합니다. 이벤트 루프는 사용자 입력과 이벤트를 수신하고 이에 대응하여 적절한 조치를 취하는 연속 루프

