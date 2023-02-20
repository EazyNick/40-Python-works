#클래스, 객체 개념을 이해하면 이해가능. 함수 여러개를 합쳐 놓은 클래스를 예시로 알면 좋다.
class Greet(): #인사를 하는 클래스
    def hello(self): #클래스 안에 있는 함수는 메쏘드 라고 부름
        print("hello")
    def hi(self):
        print("hi")

human1 = Greet() #Greet안의 기능을 수행하기위해 human1값에 넣어줌.
human1.hello() # Greet안의 hello 함수 실행
human1.hi() # Greet안의 hi 함수 실행
human2 = Greet() # human2라는 객체도 동일. 같은 객체가 여러개일 경우 사용이 편하다
human2.hello()
human2.hi()

class Student():
    def __init__(self,name,age,like): #맨앞에 self(자기자신의 이름이다.)붙여야 한다. init은 객체를 만들떄 무조건 자동으로 실행되는 메소드이다.
        self.name = name
        self.age = age
        self.like = like
    def studenInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는것:{self.like}")
김철수 = Student("김철수",17,"축구")#변수명 한글되는데 추천은 x, 각 객체 정보 입력
장다인 = Student("정다인",6,"헬로키봇")
김철수.studenInfo()#정보 출력함수사용해 출력!
장다인.studenInfo()

class Mother(): #부모클래스
    def characteristic(self):
        print("키가크다")
        print("공부를 잘한다")
class Daugther(Mother): #가로안에 상속받을 상위클래스를 적어주면 사용가능
    def characteristic(self):
        super().characteristic() #super은 위에 상속받은 것을 실행할려고 씀.
        print("운동을 잘한다")
엄마 = Mother()
엄마.characteristic()
딸 = Daugther()
딸.characteristic()

# class Mother(): #부모클래스
#     def __init__(self):
#         print("키가크다")
#         print("공부를 잘한다")
# class Daugther(Mother): #가로안에 상속받을 상위클래스를 적어주면 사용가능
#     def __init__(self):
#         super().__init__()
#         print("운동을 잘한다")
# 엄마 = Mother() #init쓰면 불러오기만 해도 무조건 한번 실행.
# 딸 = Daugther()

#class변수와 instance 변수는 다르다. https://cafe.naver.com/cortexsh/3843?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6ImNvcnRleHNoIiwiYXJ0aWNsZUlkIjozODQzLCJpc3N1ZWRBdCI6MTY3NTc0NTE5OTU0Nn0.qyp3efrcdN607LL0VYzExFyKLyJAqS22CfRdMh9jTlA
#class바로 아래에 변수를 써주면 class끼리 변수를 공유할 수 있다. 하지만 메서드 아래에 변수를 써주면 같은class끼리 변수공유는 하지않는다.
