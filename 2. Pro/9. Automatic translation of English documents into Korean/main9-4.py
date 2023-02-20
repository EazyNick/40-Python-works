#영어로된 문장을 한글로 번역 후 다른 파일로 저장.
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"40 Python works\9. Automatic translation of English documents into Korean\En.txt" #상대경로 복사
write_file_path = r"40 Python works\9. Automatic translation of English documents into Korean\Ko.txt" #여기다가 쓸꺼에요

#read_file_path 는 파일 경로를 지정한 변수이다.
with open (read_file_path, 'r') as f : #파일을 읽기 형식으로 열고 그 파일을 f라고 하겠다.
    readLines = f.readlines() #파일을 읽고 그값을 readLines에 넣어주겠다.

for lines in readLines: #readlines값들을 lines안에 넣고 readlines들 값만큼 반복.
    result1 = translator.translate(lines, dest='ko') #한국어로 해석하고 번역.
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f: #쓰기 형식으로 파일을 UTF8(한국어)방식으로 열고 이것을  f라 칭한다.
        f.write(result1.text + '\n')# 이것을 쓴다. \n은 한줄 띄워서 파일에 작성시킴.
