#55:11

import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nado game")

# FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background_img = pygame.image.load("C:\\pygame\\pygame_basic\\bam.jpg")

#(캐릭터)스프라이트 불러오기
character = pygame.image.load("C:/pygame/pygame_basic/whiteham.jpg")
character_size = character.get_rect().size   #이미지의 크기를 구해옴
character_width = character_size[0]

character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)   #화면 가로 절반 크기에 해당하는 위치
character_y_pos = screen_height-70   #화면 세로 크기 가장 아래에 해당하는 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\pygame\\pygame_basic\\paintingham.jpg")
enemy_size = enemy.get_rect().size   #이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)   #화면 가로 절반 크기에 해당하는 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2)  #화면 세로 크기 가장 아래에 해당하는 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

#총 시간
total_time = 10

#시작 시간 정보
start_ticks = pygame.time.get_ticks()

#이벤트 루프
running = True # 게임 진행 여부
while running:

    dt = clock.tick(120) #게임 프레임 수

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는 지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0: 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계값 처리
    if character_y_pos < 0: 
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 캐릭터 rect(위치) 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # screen.fill((0, 0, 255))
    screen.blit(background_img, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    #타이머 
    #경과 시간 계산(단위: ms)
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    #출력할 글자, True, 글자 색상
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    #시간이 0이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() #게임화면을 다시 그리기
    
    #잠시 종료 대기(단위 ms)
    pygame.time.delay(2000)
#pygame 종료
pygame.quit()