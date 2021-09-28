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
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로 절반 크기에 해당하는 위치
character_y_pos = screen_height-70 #화면 세로 크기 가장 아래에 해당하는 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.5

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

    # screen.fill((0, 0, 255))
    screen.blit(background_img, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()