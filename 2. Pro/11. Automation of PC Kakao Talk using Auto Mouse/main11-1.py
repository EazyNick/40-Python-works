#오토마우스를 활용한 PC카카오톡 자동화
#schedule라이브러리는 일정시간마다 함수를 동작시킬때 활용 ex)언제마다 뭘해야댈때

import pyautogui #특정한 이미지 찾기 가능

picPosition = pyautogui.locateOnScreen(r'40 Python works\11. Automation of PC Kakao Talk using Auto Mouse\카카오톡_내사진1.png')
#locateOnScereen에 한번 사진을 등록해놓으면 그 사진을 똑같이 찾아서 포지션을 알려줌.
print(picPosition) #화면에 같은 사진이 있다면 좌표를 출력함.

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen(r'40 Python works\11. Automation of PC Kakao Talk using Auto Mouse\카카오톡_내사진2.png')
#     print(picPosition)

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen(r'40 Python works\11. Automation of PC Kakao Talk using Auto Mouse\카카오톡_내사진3.png')
#     print(picPosition)
