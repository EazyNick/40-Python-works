# 파이썬의 기본 문법 익히기
#사칙연산 +
print("더하기:", 10+20)
print("빼기:", 10-20)
print("곱하기:", 10*20)
print("나누기:", 10/20)

#거듭제곱 *
print("**2", 10**2) #10의 2제곱
print("**3",10**3) #10의 3제곱
print(1024**3) #1024의 3제곱 = 1024*1024*1024

#몫과 나머지 /, %
print("몫:", 40/6) # 6
print("나머지:", 40%6) # 4

#논리 연산 and, or, not
#and - 모든 조건이 참이면 참
#or - 조건중에 하나라도 참이면 참
#not - 참 -> 거짓, 거짓 -> 참
print(0 or 0) # 0
print(0 or 1) # 1
print(0 and 0) # 0
print(0 and 1) # 0
print(1 and 1) # 1
print(False and False) # False, 숫자0은 False, 1이상이면 True이다.
print(False and True) # False
print(True and True) # True
print(10 and 0) # 0
print(not 0) # True
print(not 1) # False
print(not True) # False
print(not False) # True

#비교 연산(조건식에서 사용), =(대입 연산)이랑 ==(이퀄, 같다)은 다르다. ==, <=, >=, <, >
print(10 == 10) # True
print(10 >= 10) # True
print(10 <= 10) # True
print(10 < 10) # False
print(10 != 10) # Flase, 같지않으면 True임. !은 NOT

a_list = ['a', 2, 'hello', 3]
print('a' in a_list) #a_list에 'a'가 포함되어 있으면 True 출력. 아니면 False 출력
a_str = "hello python" #역시 a_str말고 다른거 써도됨. 변수의 이름임!
print("python" in a_str) #python이 있으면 True
print("py" in a_str) #py가 있으니 True
print("40" in a_str) #40 없으니 False
print("python" not in a_str) # 포함되어 있지 않아야 True, 그러므로 False가 출력댐.
