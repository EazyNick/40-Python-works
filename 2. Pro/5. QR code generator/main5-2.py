#파일을 불러오겠다.
import qrcode

#3-3에서 txt파일 읽는것 가져옴. 경로만 바꿔주면 재사용 가능.
file_path = r'40 Python works\5. QR code generator\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f: #with구문으로 파일을 열어보자. 'rt'는 리드 텍스트 파일. 읽기모드로 하겠다.
    read_lines = f.readlines() #한국어는 UTF8이다. 그리고 이것을 f로 불러다 사용하겠다. readlines는 여러줄을 읽겠다. 리스트 형태로 반환됨.
    for line in read_lines:
        line = line.strip() #공백제거, 우리가 기본적으로 문장 쓰면 맨뒤에 공백하나 있음.
        print(line)

