import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

# 플레이어 클래스 만들기
class Player():
# 객체를 생성할 때 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

# 파란색의 네모를 x,y 좌표헹 40X40 사이즈로 그림/ 반환하는 값은 좌표의 크기
    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

# 플레이어의 점프를 구현
    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

# Enemy(적) 클래스 생성
class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))

# 화면의 오른쪽 끝에서부터 왼쪽으로 이동하는 함수
    def move(self,speed):
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH

player = Player(50, MAX_HEIGHT - 40)
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40) # Enemy의 이름으로 객체 생성/ 시작위치는 오른쪽 끝

def main():
    speed = 7 # 적의 속도를 초기 7로 설정

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.Quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True

        clock.tick(FPS)
        screen.fill((255,255,255))
        player_rect = player.draw()
        player.jump()   
        enemy_rect = enemy.draw() # 적 그리기/ 적의 위치와 크기 반환

# 적의 속도는 0.01씩 점점 빨라짐
        enemy.move(speed)
        speed = speed + 0.01 

# 플레이어와 적이 충돌하면 종료
        if player_rect.colliderect(enemy_rect):
            print("충돌")
            pygame.quit()
            sys.exit()
        pygame.display.update()

if __name__ == '__main__': 

    main()        

