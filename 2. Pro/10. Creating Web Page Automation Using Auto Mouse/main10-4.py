#여러 지역 한번에 검색
import pyautogui
import time
import pyperclip

날씨 = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨"]

addr_x = 470
addr_y = 239
start_x = 119
start_y = 363
end_x = 765
end_y = 659

for regional_weather in 날씨:
    pyautogui.moveTo(addr_x, addr_y, 1)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("www.naver.com", interval=0.1)
