#쓰레드란?
#프로세스 : 운영체제로부터 자원을 할당받는 자원의 단위 (보통 프로그램 1개)
#쓰레드 : 프로세스가 할당받은 자원을 이용하는 실행의 단위 (프로그램 1개에서 여러기능을 수행해야하므로 한 프로그램에 여러 쓰레드 필요.)

import threading #기본 라이브러리
import time #시간지연

def thread_1 ():
    while True:
        print("쓰레드 1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1) #나는 target = ??, ??함수를 쓰레드로 지정한다.
t1.start() #한번 시작해놓으면 메인동작과 별개로 계속 동작한다.

while True:
    print("메인동작")
    time.sleep(2.0)