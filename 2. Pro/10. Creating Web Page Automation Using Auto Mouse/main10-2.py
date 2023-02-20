#서울날씨 네이버 검색 자동화.
import pyautogui
import time
import pyperclip

pyautogui.moveTo(470,239,0.2) #그 좌표로 0.2초안에 움직여라.
pyautogui.click() # 클릭
time.sleep(0.5) #0.5초 딜레이

pyperclip.copy("서울 날씨") #복사
pyautogui.hotkey("ctrl", "v") #붙여넣기
time.sleep(0.5) # 0.5초 딜레이

pyautogui.write(["enter"]) #엔터
time.sleep(1)