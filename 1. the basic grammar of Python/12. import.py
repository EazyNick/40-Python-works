#import 익히기 다른곳에서 만들어놓은 기능을 불러옴.

import random #random이라는 라이브러리에서
print(random.randint(1,10)) #randint라는 기능을 쓰겠다. 1~10까지 랜덤한 수 출력

import random as rd #나는 random이란 함수를 가져왓지만, rd로 바꿔 쓰겠다.
print(rd.randint(1,10))

from random import randint #랜덤이라는 라이브러리에서 randint기능만 쓰겠다.
print(randint(1,10))

from random import *#random에서 모든기능을 가져다 쓰겠다

print(randint(1,10))
