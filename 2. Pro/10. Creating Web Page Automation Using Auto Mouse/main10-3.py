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

start_x = 119
start_y = 363
end_x = 765
end_y = 659

pyautogui.screenshot(r'40 Python works\10. Creating Web Page Automation Using Auto Mouse\서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y)) #Pillow깔아서 고침.
