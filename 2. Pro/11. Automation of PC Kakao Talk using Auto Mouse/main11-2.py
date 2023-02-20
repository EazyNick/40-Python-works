#해당 사진을 찾고 더블클릭 후 해당 입력한 메세지를 입력 후 창을 닫는다.
import pyautogui
import pyperclip
import time

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
