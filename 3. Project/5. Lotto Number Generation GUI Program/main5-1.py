import random

lotto_num = range(1,46) #1~45까지 랜덤숫자

for i in range(5): #5번 반복
    print(random.sample(lotto_num,6)) #1~45까지 랜덤숫자 6자리 생성.
#총 리스트 5개, 숫자 총6개씩 30개 생성