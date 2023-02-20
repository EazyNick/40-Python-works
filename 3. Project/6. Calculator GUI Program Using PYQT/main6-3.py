# Qt Designer로 계산기 Widget 만들기
#  1) 아나콘다를 이용해서 파이썬을 설치하면 pyqt가 기본으로 설치되어있습니다.
#   pyqt는 designer라는 그래픽 환경의 GUI 생성 툴이 있습니다.

#  2) 터미널에 designer를 입력합니다.
#   그려면 Qt Designer 프로그램이 열립니다.

#  3) [Widget]을 선택 후 [생성] 버튼을 클릭하여 새로운 [Widget]을 생성합니다.
#   Widget이 생성되면 위젯 상자에서 가운데 위젯으로 아이콘을 끌어다 위치시켜 GUI를 구성할 수 있습니다.
#   속성 편집기에서 각각의 위젯의 속성을 변경할 수 있습니다.

# 4) 가운데 위젯을 선택 후 속성을 변경합니다.
#   geometry에서 너비와 높이를 각각 400, 500으로 설정합니다.
#   Layouts에서 [Vertical Layout]은 생성된 위젯의 위쪽에 [Grid Layout]은 아래쪽에 위치시킵니다.
#   [Input Widgets]에서 [Line Edit]를 [Vertical Layout]에 위치시킵니다.
#   [Line Edit] 속성을 아래와 같이 설정합니다.
#    - objectName: le_view
#    - font(포인트 크기): 40
#    - text: 0
#    - alignment: 오른쪽 정렬, 아래로 정렬
#   [Push Botton]을 16개를 위치시킵니다.
#   각각의 버튼을 더블클릭하거나 버튼 속성의 text를 변경하여 수정합니다.
#   각각 버튼의 ObjectName을 아래와 같이 수정하고 minimumSize의 높이는 모두 80으로 수정합니다.
#   ★ objectName은 파이썬 코드에서 사용하므로 정확하게 입력해야합니다.
#    - 7: btn_number7
#    - 8: btn_number8
#    - 9: btn_number9
#    - /: btn_divide
#    - 4: btn_number4
#    - 5: btn_number5
#    - 6: btn_number6
#    - X: btn_multipy
#    - 1: btn_number1
#    - 2: btn_number2
#    - 3: btn_number3
#    - +: btn_add
#    - C : btn_C
#    - 0: btn_number0
#    - =: btn_result
#    - -: btn_minus
#4. 수식을 계산 코드에 추가하여 계산기 코드 완성하기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = r"40 Python works\3. Project\6. Calculator GUI Program Using PYQT\계산기.ui"
form_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.le_view.setEnabled(False)

        self.text_value = "" # 클래스 내부의 변수 초기화
#사용자가 입력하고 있는 현재 입력 또는 식을 저장하는 데 사용될 수 있습니다.
    def btn_clicked(self):
        btn_value = self.sender().text()

# C 버튼이 눌렸다면 le_view의 텍스트를 0으로 초기화한 후 text_value 전역변수를 빈값으로 초기화
        if btn_value == 'C':
            print("clear")
            self.le_view.setText("0")
            self.text_value = ""

# 버튼이 눌리면 계산을 해서 값을 보여줌
        elif btn_value == '=':
            print("=")
            try:
                resultValue = eval(self.text_value.lstrip("0")) # eval은 문자열 수식을 계산한 값을 문자열로 변환합니다.
#lstrip("0")은 왼쪽의 0을 제거합니다. 001의 경우 1로 됨
                self.le_view.setText(str(resultValue)) # le_view에 계산된 값 출력
            except:
                self.le_view.setText("error")
#사용자가 잘못된 식을 입력할 때 응용 프로그램이 충돌하거나 예기치 않게 동작하는 것을 방지할 수 있습니다.

# 숫자 및 수식 값이 눌려지면 self text_value변수에 값을 더해나감/ X버튼이 눌렸다면 계산할 수 있는 *로 변경
        else:
            if btn_value == 'X':
                btn_value = '*'
            self.text_value = self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        