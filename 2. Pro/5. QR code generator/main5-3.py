#txt파일을 불러오고 안에 내용들 qr코드로 만들겠다. 실행하면 한번에 여러개의 qr코드 생성가능.
import qrcode

#3-3에서 txt파일 읽는것 가져옴. 경로만 바꿔주면 재사용 가능.
file_path = r'40 Python works\5. QR code generator\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f: #with구문으로 파일을 열어보자. 'rt'는 리드 텍스트 파일. 읽기모드로 하겠다.
    read_lines = f.readlines() #한국어는 UTF8이다. 그리고 이것을 f로 불러다 사용하겠다. readlines는 여러줄을 읽겠다. 리스트 형태로 반환됨.
    
    for line in read_lines:
        line = line.strip() #strip은 공백제거, 우리가 기본적으로 문장 쓰면 맨뒤에 공백하나 있음.
        qr_data = line #qr_data = line안쓰고 그냥 qr_data를 line으로 다 바꿔써도 된다.
        qr_img = qrcode.make(qr_data)
        save_path = r'40 Python works\5. QR code generator\\' + qr_data + '.png' #해당 경로에 이미지 저장하겠다. 확장자는 .png, \\한번해주면 오류남. 두번해주자
        qr_img.save(save_path) # 저장실행. save_path 경로, 확장자로 qr_img를 저장.  