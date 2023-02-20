#if 조건문
#if 조건식:(콜론)
#(들여쓰기 해야함, 탭이나, 스페이스 네번)
#    (내용)

#if만 사용
a = 1
b = 1
if a == b:
    print("두 개의 값은 같습니다") #a와 b값 같으면 출력.
if a !=b:
    print("두 개의 값은 같지 않습니다") #a와 b값 다르면 출력

#if else
a = 1
b = 2
if a == b:
    print("두 개의 값은 같습니다.")#a와 b값 같으면 출력
else:
    print("두 개의 값은 같지 않습니다")#a와 b값 다르면 출력

#if elif else
a = 1
b = 2
if a > b:
    print("a값이 더 큽니다") #첫조건
elif a < b:
    print("b 값이 더 큽니다") #첫조건이 틀리면 두번쨰 조건 실행
else:
    print("두 개의 값은 같습니다")# 둘다 아니면 출력

a = 1
b = 1
c = 2
d = 2
if a == b and c == d:
    print("두 조건 모두 만족") #둘다 True 여야 출력
if a == b or c== d:
    print("두 조건 중 하나라도 만족")#둘중 하나만 True 여도 출력
if 1:
    print("참") #참(1이상)이면 출력, 반대로 0하면 False면 출력
