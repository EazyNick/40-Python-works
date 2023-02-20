#txt파일을 불러와서 읽자
#.txt파일 상대적인 경로 복사해서 붙여넣기 하면 된다.

from gtts import gTTS #gtts라이브러리에서 gTTS만 가져오겠다.
from playsound import playsound #playsound로부터 playsound를 불러와 사용하겠다.

file_path = r'40 Python works\3. Converting text to speech\my text.txt'
with open(file_path, 'rt', encoding='UTF8') as f: #with구문으로 파일을 열어보자. 'rt'는 리드 텍스트 파일. 읽기모드로 하겠다.
    read_file = f.read() #한국어는 UTF8이다. 그리고 이것을 f로 불러다 사용하겠다.

#txt파일 내용들을 file_path에 담고, 그파일을 'rt'방식으로 'UTF8'언어로 열고, 그것을 f라고 지정한다.
#그리고 f.read() 파일을 읽고 그것을 read_file에 저장한다..

# print(read_file) 하면 txt파일 문장들 실행됨.

tts = gTTS(text=read_file, lang='ko') #읽은 내용들을 음성으로 저장.
tts.save(r'40 Python works\3. Converting text to speech\my text.mp3') #my text.mp3가 생성된다.

playsound(r'40 Python works\3. Converting text to speech\my text.mp3') #my text.mp3를 플레이한다.

