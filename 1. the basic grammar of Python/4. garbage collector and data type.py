#고급언어의 특징으로, a = 10 후에 a = 20을 주면, 자동으로 쓸모없어진 10을 버리는거
#메모리를 절약함.

#자료형
#변수는 하나의 값만 가질 수 있지만 자료형은 변수 하나에 이름에 여러 값을 가질 수 있다.
a_list = [1,2,3,4,5] #[]가 리스트, 0번쨰, 1,2,3,4번쨰 자리값!
print(a_list) #[1, 2, 3, 4, 5] 출력
print(a_list[0]) # 1출력
print(a_list[1]) # 2출력
print(a_list[-1]) # 5출력, -2,-3도됨

print(a_list[:2]) #[1 ,2] 출력 2번쨰 전까지 출력! 2미만
print(a_list[2:]) #[3, 4, 5] 출력, 2초과, 이것들을 슬라이싱 이라함

#리스트 list 내용추가하기.
b_list = []
b_list.append(1)
b_list.append(3)
b_list.append(4)
print(b_list) #[1, 3, 4] 출력

c_list = [1,3.14,"hello",[1,2,3]] #리스트안에 숫자, 문자, 리스트 다 저장가능. 여러 타입 저장 가능
print(c_list) # [1, 3.14, 'hello', [1,2,3]] 출력
print(c_list[1:3]) #[3.14, 'hello']

d_list = [1,2,3,4,5]
print(d_list)
d_list[0] = 5 # 0번쨰의 값을 5로 바꿈
print(d_list) #[5, 2, 3, 4, 5] 출력

#튜플 값 변경 불가 tuple
a_tuple = (1,2,3,4,5)
print(a_tuple) #(1, 2, 3, 4, 5) 출력
#a_tuple[0] = 5 하면 오류남. 데이터가 변경되면 안될때 사용.

#키와 값이 있는 딕셔너리 dic, dic붙어서 딕셔너리가 된게 아닌, 가로안에 {'a':1, 'b':2, 'c':3}형태가 딕셔너리 형식이다. 
#앞에 a_dic대신 다른 아무거나 써도 상관없다.
a_dic = {'a':1, 'b':2, 'c':3}
print(a_dic) # {'a': 1, 'b': 2, "c": 3} 출력
print(a_dic['a']) # 1이 출력됨
print(a_dic['b']) # 2이 출력됨
print(a_dic['c']) # 3이 출력됨

b_dic = {1:'a', 'b':[1,2,3], 'c':3} #다채로운 타입으로 사용가능
print(b_dic[1]) # a 출력
print(b_dic['b']) #[1, 2, 3] 출력
print(b_dic['c']) # 3 출력

b_dic['d'] = 4
print(b_dic) # 'd': 4가추가됨.

#중복이 없는 자료형, 순서가 없이 저장되는 set
a_set = set([1,2,3,4])
print(a_dic) # {1, 2, 3, 4} 출력
b_set = set([1,1,2,2,3,3,4,4,5,6])
print(b_set) # {1, 2, 3, 4, ,5, 6} 출력

c_set = set("python40s") #순서가 없다.
print(c_set) #{'n', 'p', '0', 'y', 'h', 't', '4', '0', 's'}가 출력됨

#List, tuple, dictionary, set 4종류 알아두자!