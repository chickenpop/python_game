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

#이벤트 루프
running = True # 게임 진행 여부
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False
    
    # screen.fill((0, 0, 255))
    screen.blit(background_img, (0, 0)) #배경 그리기
    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()