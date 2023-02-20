#쓰레드의 동작원리를 알아보는 코드이다.
#쓰레드는 자신이 먼저 실행되고 싶어해서 순서가 뒤죽박죽이다. 경쟁적으로 동작함.
#main8-3이라는 프로세스를 할당받아. 쓰레드를 나눔.
import threading

def sum(name, value): #value값은 ?번 출력.
    for i in range(0, value):
        print(f"{name} : {i}")

t1 = threading.Thread(target=sum, args=('1번쓰레드', 10)) #args=을빼도 동작함.
t2 = threading.Thread(target=sum, args=('2번쓰레드', 10))

t1.start()
t2.start()

print("Main Thread")