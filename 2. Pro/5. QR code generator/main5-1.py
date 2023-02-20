#QR코드 생성하자. 여러개를 만들때 파이썬을 활용. 한개만 만들꺼면 그냥 인터넷에 qr코드 만들기 쓰면 나옴.
import qrcode

qr_data = 'www.naver.com' #네이버 사이트 qr코드 생성
qr_img = qrcode.make(qr_data) #qr데이터를 넣어 이미지 불러옴.

save_path = r'40 Python works\5. QR code generator\\' + qr_data + '.png' #해당 경로에 이미지 저장하겠다. 확장자는 .png, \\를 뒤에 붙여 5. QR code generator 폴더 안에 저장.
qr_img.save(save_path) # 저장실행. save_path 경로, 확장자로 qr_img를 저장.

