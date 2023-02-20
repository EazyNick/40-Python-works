import pyautogui
import pyperclip
import time
import schedule

def send_message():
    picPosition = pyautogui.locateOnScreen(r"40 Python works\11. Automation of PC Kakao Talk using Auto Mouse\카카오톡_내사진1.png")
    print(picPosition)

    clickPostition = pyautogui.center(picPosition) #사진위치 클릭, 원래 pyautogui.center인데 오류나면 click으로 바꾸자.
    pyautogui.doubleClick(clickPostition) # 더블클릭
    time.sleep(2.0)

    pyperclip.copy("이 메세지는 자동으로 보내는 메시지 입니다~~") #복사
    pyautogui.hotkey("ctrl", "v") #붙여넣기
    time.sleep(1.0)

    pyautogui.write(["enter"]) #엔터
    time.sleep(1.0)

    pyautogui.write(["escape"]) #탈출
    time.sleep(1.0)

schedule.every(10).seconds.do(send_message) #매 10초마다 send_message함수를 실행.

while True:
    schedule.run_pending() #스케줄을 계속 동작시킬려면 while문 안에 있어야함.
    time.sleep(1)
