import pygame
import os
######################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 설정
screen_width = 1890
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("cuphead hamster")

# FPS
clock = pygame.time.Clock()
######################################################################################################
# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 etc...)

current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")

#배경만들기
background = pygame.image.load(os.path.join(image_path, "C:\\pygame\\cuphead\\images\\background.jpg"))

#stage 만들기
stage = pygame.image.load(os.path.join(image_path, "C:\\pygame\\cuphead\\images\\stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "C:\\pygame\\cuphead\\images\\character.jpg"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동 방향
character_to_x = 0
character_to_y = 0

#캐릭터 이동 속도
character_speed = 5

#보스 만들기
boss = pygame.image.load(os.path.join(image_path, "C:\\pygame\\cuphead\\images\\boss.jpg"))
boss_size = boss.get_rect().size
boss_width = boss_size[0]
boss_height = boss_size[1]
boss_x_pos = screen_width - (boss_width/2)
boss_y_pos = screen_height - boss_height - stage_height

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "C:\\pygame\\cuphead\\images\\weapon.jpg"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 연사
weapons = []

# 무기 연사 속도
weapon_speed = 10 

running = True # 게임 진행 여부
while running:

    dt = clock.tick(120) #게임 프레임 수
    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_UP:
                character_to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                character_to_y += character_speed
            elif event.key == pygame.K_z: #키 발사
                weapon_x_pos = character_x_pos + (character_width/2) + (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    character_y_pos += character_to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - stage_height - character_height:
        character_y_pos = screen_height - stage_height - character_height

    # 무기 위치 조정
    # 100(x), 200(y) -> 180, 160, 140 ... y에 weapon_speed를 빼는 이유
    weapons = [ [w[0] + weapon_speed, w[1]] for w in weapons] #무기 위치를 위로 올림

    # y = 0 무기 제거
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
    
    # 4. 충돌 처리

    # 5. 화면에 그리기 
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height -stage_height))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(boss, (boss_x_pos, boss_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()