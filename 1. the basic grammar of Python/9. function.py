#함수 = 기능의 단위
def func(): #이것은 정의만 해서 출력하면 아무것도 안나옴. 불러와야 댐.
    print("안녕하세요")
    print("파이썬과 40개의 작품들 입니다.")
func()
for i in range(3):
    func()

def funcAdd(a,b):
    return a+b
c = funcAdd(1,2)
print(c)

def funcMux(a,b):
    return a*b
c = funcMux(1,2)
print(c)

def funcAddMux(a,b):
    add = a+b
    mux = a*b
    return add, mux

a,b = funcAddMux(1,3)
print(a)
print(b)
_,b = funcAddMux(1,3) #b값만 받겠다 할때 a자리에 _해도됨.
print(b)
b = funcAddMux(1,3)[1] #리스트 처럼 나는 2번째 값만 받겠다. [1]을 뺴면 (4,3)이 출력됨.
print(b)