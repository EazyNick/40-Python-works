import tkinter
import tkinter.font
import random

lotto_num = range(1,46) #1~45 리스트 만들어 lotto_num 넣음.

def buttonClick(): 
    for i in range(5):
        lottoPick = map(str, random.sample(lotto_num, 6))
        lottoPick = ','.join(lottoPick)#문자열 리스트를 합쳐서 하나의 문자열로 변환, 중간에 ,추가
        lottoPick = str(i+1) + "회: " + lottoPick
        print(lottoPick) #터미널에 보여줌. 안써도됨.
        listbox.insert(i, lottoPick) #리스트박스에 값 넣기
    listbox.pack()

window=tkinter.Tk() #window 객체생성
window.title("lotto") #타이틀 정의
window.geometry("400x200+800+300") #GUI사이즈 설정 400x200사이즈에 처음시작하는 위치가 +800+300설정
window.resizable(False, False) #가로세로의 크기를 조절하지 못하도록 설정

button = tkinter.Button(window, overrelief="solid", text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=1000)
#overrelief는 버튼에 마우스를 올렸을 때 버튼의 테두리 모양, text=버튼에 표시할 문자열, width=버튼의 너비, command = 선택시 함수 실행 시킬 수 있음.
#repeatdelay=버튼이 눌러진 상태에서 command 실행까지의 대기시간(ms), repeatinterval=버튼이 눌러진 상태에서 command 실행의 반복 시간(ms)
button.pack() #버튼을 배치한다.

#리스트 박스 생성
font = tkinter.font.Font(size=20)
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)
#extended는 다중선택, 마우스 드래그나 쉬프트키 + 방향키 이동으로 선택.
listbox.insert(0, "1회:")
listbox.insert(1, "2회:")
listbox.insert(2, "3회:")
listbox.insert(3, "4회:")
listbox.insert(4, "5회:")
listbox.pack()

window.mainloop() #종료하지 않고 화면계속 유지