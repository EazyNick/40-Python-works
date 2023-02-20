import itertools #passwd_string = "?" ?안에 것들을 모두 경우의수로 돌려봄
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile): #함수로 만들면 탈출할 수 있다. zFile은 파일 형식이다.
    for len in range(min_len, max_len+1): #1~5자리까지 돌려봄. +1해줌으로 더 편하게 사용가능. 5를 넣으면 1~5까지 찾아줌.
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode()) #extractall압축을 풀겠다, encode 패스워드 입력해봄 맞으면 다음문장으로, 틀리면 except문장으로 감.
                print(f"비밀번호는 {passwd} 입니다.")
                return 1 #return은 무조건 함수를 끝냄. 고로 for문도 끊어짐. 
            except:
                pass #맞으면 비밀번호를 알려주고 틀리면 에러가 나서 패스를 해줌. 

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r"40 Python works\6. Compressed file decryption program\암호는 1234.zip")

min_len = 1
max_len = 5

un_zip_result = un_zip(passwd_string, min_len, max_len, zFile) # 함수 사용

if un_zip_result == 1: #return 1값을 반환해주므로 == 1이다.
    print("암호찾기에 성공하였습니다.")
else:
    print("암호찾기에 실패하였습니다.")
