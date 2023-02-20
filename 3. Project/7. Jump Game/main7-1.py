#파이썬은 객체 지향 언어이다.
#게임화면 구성하고 스페이스바를 입력받는 코드 만들기
import pygame
import sys

FPS = 60 #1초에 60 프레임 작동
MAX_WIDTH = 600
MAX_HEIGHT =400

pygame.init() # 파이게임 초기화
clock = pygame.time.Clock() # clock 설정
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT)) # 스크린 설정 600 X 400 픽셀로 설정

def main():
    while True:
        for event in pygame.event.get(): # 파이게임의 이벤트 가져오기, 마우스, 키보드 입력값을 받을 수 있음.

# [X] 버튼 누르면 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 키 다운 입력 중에 스페이스바 눌리면 space 출력
            if event.type == pygame.KEYDOWN: #키보드를 눌렀을 경우
                if event.key == pygame.K_SPACE: # 그게 스페이스바일 경우
                    print("space")

        clock.tick(FPS) # FPS 설정/ 1초에 몇 프레임 작동할지 경정/ 60FPS 동작
        screen.fill((255, 255, 255)) # 화면 흰색으로 채우기 RGB형식임.

        pygame.display.update() # 화면 그리기

if __name__ == '__main__':

    main()                      
