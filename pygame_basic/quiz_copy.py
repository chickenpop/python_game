import pygame
from pygame.constants import K_LEFT
from random import *

######################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 etc...)
backgroud = pygame.image.load("C:\\pygame\\pygame_basic\\fly_ham_me.jpg")

# 캐릭터 만들기
character = pygame.image.load("C:\\pygame\\pygame_basic\\paintingham.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# 적 캐릭터 만들기
dislike = pygame.image.load("C:\\pygame\\enemy.png")
dislike_size = dislike.get_rect().size
dislike_width = dislike_size[0]
dislike_height = dislike_size[1]
dislike_x_pos = randint(0, screen_width-dislike_width)
dislike_y_pos = 0
dislike_speed = 10

#이동 위치
to_x = 0
character_speed = 10

running = True # 게임 진행 여부
while running:

    dt = clock.tick(30) #게임 프레임 수
    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    dislike_y_pos += dislike_speed
    if dislike_y_pos > screen_height:
        dislike_y_pos = 0
        dislike_x_pos = randint(0, screen_width-dislike_width)


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    dislike_rect = dislike.get_rect()
    dislike_rect.left = dislike_x_pos
    dislike_rect.top = dislike_y_pos

    if character_rect.colliderect(dislike_rect):
        print("충돌함")
        running = False

    # 5. 화면에 그리기 
    screen.blit(backgroud, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(dislike, (dislike_x_pos, dislike_y_pos))

    pygame.display.update() #게임화면을 다시 그리기
    
#pygame 종료
pygame.quit()