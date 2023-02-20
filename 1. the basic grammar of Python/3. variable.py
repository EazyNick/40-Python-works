#변수
a = 10
b = 10
c = a + b # 프린트하면 20나옴, =은 오른쪽의 값을 왼쪽에 매칭하라란 뜻이다.
print(c)

d = '10' #''안에 넣으면 문자열
#문자열과 숫자열은 더할수 없다. print(c+d) 하면 에러
print(c+int(d)) #프린트 하면 30나옴

e = 3.14
f = 10 #소수와 숫자는 더할 수 있다.
print(e + f)

a = 10
b = 10
c = float(a) + float(b)
print( c ) # 20나옴

a_bool = True
b_bool = False
a_int = 1
b_int = 0
print(a_bool) #True
print(b_bool) #False
print(type(a_bool)) #<class 'bool'> 타입 확인 가능
print(type(b_bool)) #<class 'bool'>
print(a_int) #1
print(b_int) #0
print(type(a_int)) #<class 'int'>
print(type(b_int)) #<class 'int'>
