#영어문서를 해석하기.
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"40 Python works\9. Automatic translation of English documents into Korean\En.txt" #상대경로 복사
#read_file_path 는 파일 경로를 지정한 변수이다.
with open (read_file_path, 'r') as f : #파일을 읽기 형식으로 열고 그 파일을 f라고 하겠다.
    readLines = f.readlines() #파일을 읽고 그값을 readLines에 넣어주겠다.

for lines in readLines: #readlines값들을 lines안에 넣고 readlines들 값만큼 반복.
    result1 = translator.translate(lines, dest='ko') #한국어로 해석하고 번역.
    print(result1.text)