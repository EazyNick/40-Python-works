import random
random_number = random.randint(1,100)
#print(random_number)

game_count = 1

while True: #게임이 끝나지 않게 반복, 맞춰도 반복.
    my_number = int(input("1~100사이의 숫자를 입력하세요:")) # 만약 int정수형이 아닌 값을 입력하면 안됨.
    if my_number > random_number:
        print("다운")
    elif my_number < random_number:
        print("업")
    elif my_number == random_number:
        print(f"축하합니다. {game_count}회 만에 맞췄습니다.") #f하고 가로안에 변수를 넣어주면 그 값을 넣어준다.

    game_count = game_count + 1