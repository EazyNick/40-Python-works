#압축파일의 암호를 푸는 프로그램, 6-1에선 모든 경우의수를 출력하는 것만 진행.
import itertools # 아래 passwd_string에 입력된 값들의 모든 경우의 수를 만들어줌.

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #

for len in range(1,5):
    to_attempt = itertools.product(passwd_string, repeat = len) #len(패스워드 길이)를 입력해주면 이 길이만큼 모든 경우의수를 입력해줌.
    for attempt in to_attempt:
        passwd =''.join(attempt) #리스트를 합쳐서 문자열로 나타내줌. .join.py참고
        print(passwd)