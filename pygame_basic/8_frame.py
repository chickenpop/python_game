import pygame
######################################################################################################
# �⺻ �ʱ�ȭ (�ݵ�� �ؾ��ϴ� �͵�)
pygame.init() #�ʱ�ȭ

#ȭ�� ũ�� ����
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("nado game")

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. ����� ���� �ʱ�ȭ(���ȭ��, ���� �̹���, ��ǥ, �ӵ�, ��Ʈ etc...)
#����̹��� �ҷ�����
background_img = pygame.image.load("C:\\pygame\\pygame_basic\\bam.jpg")

#(ĳ����)��������Ʈ �ҷ�����
character = pygame.image.load("C:/pygame/pygame_basic/whiteham.jpg")
character_size = character.get_rect().size   #�̹����� ũ�⸦ ���ؿ�
character_width = character_size[0]

character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)   #ȭ�� ���� ���� ũ�⿡ �ش��ϴ� ��ġ
character_y_pos = screen_height-70   #ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ��ġ

#�̵��� ��ǥ
to_x = 0
to_y = 0

#�̵� �ӵ�
character_speed = 0.5

# �� enemy ĳ����
enemy = pygame.image.load("C:\\pygame\\pygame_basic\\paintingham.jpg")
enemy_size = enemy.get_rect().size   #�̹����� ũ�⸦ ���ؿ�
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)   #ȭ�� ���� ���� ũ�⿡ �ش��ϴ� ��ġ
enemy_y_pos = (screen_height/2) - (enemy_height/2)  #ȭ�� ���� ũ�� ���� �Ʒ��� �ش��ϴ� ��ġ

# ��Ʈ ����
game_font = pygame.font.Font(None, 40) #��Ʈ ��ü ����(��Ʈ, ũ��)

#�� �ð�
total_time = 10

#���� �ð� ����
start_ticks = pygame.time.get_ticks()
######################################################################################################


running = True # ���� ���� ����
while running:

    dt = clock.tick(120) #���� ������ ��
    # 2. �̺�Ʈ ó�� (Ű����, ���콺)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #â�� X��ư�� Ŭ����
            running = False
    # 3. ���� ĳ���� ��ġ ����
    
    # 4. �浹 ó��

    # 5. ȭ�鿡 �׸��� 

    pygame.display.update() #����ȭ���� �ٽ� �׸���
    
    #��� ���� ���(���� ms)
    pygame.time.delay(2000)
#pygame ����
pygame.quit()