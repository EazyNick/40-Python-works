#random.random() - 0.0에서부터 0.999999사이의 실수를 반환합니다.
#random.uniform(a,b) - a와 b사이의 실수값을 반환한다.
#random.randint(a,b) - a와 b사이의 정수값을 반환합니다.
#random.randrange(a,b) - a와 b사이의 정수값을 반환합니다. b값은 포함하지 않는다.
#random.randrange(a) - 인자가 하나일경우 0부터 a사이의 정수값을 반환합니다.
#random.choice(type) - type에는 문자열, 리스트, 튜플,range의 값을 입력받을 수 있고 무작위로 하나의 원소를 뽑습니다

import random
random_number = random.randint(1,100)
print(random_number)