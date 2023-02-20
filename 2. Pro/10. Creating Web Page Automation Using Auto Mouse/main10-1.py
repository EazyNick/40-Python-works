#pyautogui는 마우스와 키보드를 자동으로 제어
#pyperclip는 pyautogui가 한글이 지원되지 않아 클립보드(복사 붙여넣기)를 이용하여 한글을 사용.

import pyautogui
import time

while True:
    print(pyautogui.position())
    time.sleep(0.1) #현재 내 마우스 위치를 표시.
