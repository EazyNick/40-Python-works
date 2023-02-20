#반복문
for i in range(7): #range는 연속되는 값 만들어줌. 0~6까지 반복실행 1~6만들어줌
    print(i) #0~6까지 출력
for i in range(5,10): #5~9까지 출력
    print(i)
for i in range(5,10,-1): #10부터 6까지 역순으로
    print(i)
a_list =[1,2,3,4,5,"안녕","하세요"]
for i in a_list:
    print(i) #list 각 값을 하나씩 꺼내서 출력
a_str = "hello python"
for i in a_str: #문자도 하나씩 꺼냄.
    print(i)

name_list = ["홍길동","장다인","김철수"]
age_list = [500,5,12] #이거 안쓰는데 왜넣은거지? ㅋㅋ 강의하시는분이 실수인가봅니다.
for i,k in enumerate(name_list): #enumerate하면 몇번쨰 자리(번호값)인지와 요소가 나옴.
    print(i, end='') #end붙이면 줄바뀜 안함.
    print(k)
    print(len(name_list)) #길이를 알아냄
for i in range(len(name_list)): # list값의 수만큼 반복
    print(name_list[i])

test_list = [i*5 for i in range(10)] #0~9, 즉 9번 반복해서 i*5값을 test_list 리스트 함수로 만듬
print(test_list)

test2_list = []
for i in range(10): #위의 식과 같은 식
    test2_list.append(i*5) #append는 추가하다. 리스트에 값 추가
print(test2_list)

#while 반복문
#while True:
    #print("참이면 반복") #무한반복

a = 0
while a < 5:
    print(a)
    a = a + 1 # 한번 실행시 1씩 더해서 4까지 실행.

a = 0 #무한 반복을 하다 특정 조건을 만나면 break로 while문을 탈출
while True:
    print(a)
    a = a + 1
    if a>=5:
        break



