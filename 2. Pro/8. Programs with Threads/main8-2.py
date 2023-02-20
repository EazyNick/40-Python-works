import threading #기본 라이브러리
import time #시간지연

def thread_1 ():
    while True:
        print("쓰레드 1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1) #나는 target = ??, ??함수를 쓰레드로 지정한다.
t1.daemon = True #이걸 넣어주면 메인동작이 동작할떄만 동작하게 만듬. 이전것은 메인동작 멈춰도 파이썬을 꺼줘야 쓰레드가 멈춤.
#어차피 메인이 없으면 쓰레드도 의미 없기에 사용함.
t1.start() #한번 시작해놓으면 메인동작과 별개로 계속 동작한다.

while True:
    print("메인동작")
    time.sleep(2.0)