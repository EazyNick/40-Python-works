import tkinter
import tkinter.font
import random

lotto_num = range(1,46) #1~45 리스트 만들어 lotto_num 넣음.

def buttonClick(): 
    print(random.sample(lotto_num, 6))

window=tkinter.Tk() #window 객체생성
window.title("lotto") #타이틀 정의
window.geometry("400x200+800+300") #GUI사이즈 설정 처음시작하는 위치가 +800+300설정
window.resizable(False, False) #가로세로의 크기를 조절하지 못하도록 설정

button = tkinter.Button(window, overrelief="solid", text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=1000)
#overrelief는 버튼에 마우스를 올렸을 때 버튼의 테두리 모양, text=버튼에 표시할 문자열, width=버튼의 너비, command = 선택시 함수 실행 시킬 수 있음.
#repeatdelay=버튼이 눌러진 상태에서 command 실행까지의 대기시간(ms), repeatinterval=버튼이 눌러진 상태에서 command 실행의 반복 시간(ms)
button.pack() #버튼을 배치한다.
#누름->동작1->동작2->동작3->동작4->동작5->뗌
#repeatdelay는 [누름]과 [동작1]의 사이의 시간
#repeatinterval은 [동작1]이후에 [뗌]까지 명령어가 반복수행되는 간격
window.mainloop() #종료하지 않고 화면계속 유지