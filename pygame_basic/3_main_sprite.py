import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nado game")

#배경이미지 불러오기
background_img = pygame.image.load("C:\\pygame\\pygame_basic\\bam.jpg")

#(캐릭터)스프라이트 불러오기
character = pygame.image.load("C:/pygame/pygame_basic/whiteham.jpg")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로 절반 크기에 해당하는 위치
character_y_pos = screen_height-70 #화면 세로 크기 가장 아래에 해당하는 위치

#이벤트 루프
running = True # 게임 진행 여부
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
    
    # screen.fill((0, 0, 255))
    screen.blit(background_img, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()