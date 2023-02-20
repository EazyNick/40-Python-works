import itertools #passwd_string = "?" ?안에 것들을 모두 경우의수로 돌려봄
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r"40 Python works\6. Compressed file decryption program\암호는 1234.zip")

for len in range(1,6): #1~5자리까지 돌려봄.
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd = passwd.encode()) #extractall압축을 풀겠다, encode 패스워드 입력해봄 맞으면 다음문장으로, 틀리면 except문장으로 감.
            print(f"비밀번호는 {passwd} 입니다.")
            break #찾으면 바로 위에 for문만 탈출하고, for len in range(1,6)은 탈출하지 못해서 비밀번호 순식간에 알려주고 계속 숫자 나열됨. 이를 mian6-3에서 고쳐보자
        except:
            pass #맞으면 비밀번호를 알려주고 틀리면 에러가 나서 패스를 해줌. 
