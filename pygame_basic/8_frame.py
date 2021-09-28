import pygame
######################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nado game")

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 etc...)
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
######################################################################################################


running = True # 게임 진행 여부
while running:

    dt = clock.tick(120) #게임 프레임 수
    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리

    # 5. 화면에 그리기 

    pygame.display.update() #게임화면을 다시 그리기
    
    #잠시 종료 대기(단위 ms)
    pygame.time.delay(2000)
#pygame 종료
pygame.quit()