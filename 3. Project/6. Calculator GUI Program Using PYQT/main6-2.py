#3. 버튼 입력받아 출력하는 코드 만들기 (터미널에 버튼의 텍스트 값이 출력됨)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
ui_path = r"40 Python works\3. Project\6. Calculator GUI Program Using PYQT\계산기.ui"
form_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# 각각의 버튼을 클릭하여 btn_clicked 함수가 실행 
        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)
        self.le_view.setEnabled(False) # le_view는 글을 입력하지 못하게 함

# 각각의 버튼을 누르면 버튼의 텍스트 값을 출력
    def btn_clicked(self):
        btn_value = self.sender().text()
        print(btn_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        