import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nado game") 

#이벤트 루프
running = True # 게임 진행 여부
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창에 X버튼을 클릭함
            running = False

#pygame 종료
pygame.quit()