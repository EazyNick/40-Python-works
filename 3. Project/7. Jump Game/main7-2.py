#3. 게임 플레이어 만드는 코드 만들기
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

player = Player(50, MAX_HEIGHT - 40) # player의 이름으로 객체를 생성/ x좌표는 50 y 좌표는 바닥/ 바닥면으로 붙이기 위해 높이에서 자신의 y 크기만큼 빼줌/ y 좌표는 위부터 0임

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump =True # 스페이스 키를 입력 받으면 점프변수를 참으로 설정

        clock.tick(FPS)
        screen.fill((255,255,255))
        player_rect = player.draw() # 플레이어 그리기/ 반환하는 값은 좌표의 크기
        player.jump() # 점프 구현/ player.isjump 변수가 참이어야 동작 즉 스페이스바를 누를 때 동작
        print(player_rect)

        pygame.display.update()

if __name__ == '__main__':

    main()