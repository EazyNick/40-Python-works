from gtts import gTTS #gtts라이브러리에서 gTTS만 가져오겠다.
from playsound import playsound #playsound로부터 playsound를 불러와 사용하겠다.

text = "안녕하세요. 파이썬과 40개의 작품들 입니다." 

tts = gTTS(text = text, lang="ko") #lang=ko 는 언어는 한국어로
tts.save(r"파이썬과 40개의 작품들\3. 텍스트를 음성으로 변환하기\hi.mp3") #경로저장, 윈도우에서의 경로는 역슬래시 하고 입력하면 됨.\hi.mp3
#맨앞에 r을 붙임으로써 문자열 그대로 해석하겠다는 뜻으로, \를 아무기능으로 쓰지 않겠다 라는것을 알려줘야 오류가 안남.
#파일안에 hi.mp3라는 mp3가 생겼다. text의 문구가 저장되어서 음성으로 저장된것.

playsound(r"파이썬과 40개의 작품들\3. 텍스트를 음성으로 변환하기\hi.mp3") #이파일을 불러와서 재생해보겠다. 음성재생됨!
