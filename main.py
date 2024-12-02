import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Тир')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

target1_img = pygame.image.load('img/1.png')
target2_img = pygame.image.load('img/2.png')
target3_img = pygame.image.load('img/3.png')
target4_img = pygame.image.load('img/4.png')
bam_img = pygame.image.load('img/bam.png')

target1_img = pygame.transform.scale(target1_img, (80, 80))
target2_img = pygame.transform.scale(target2_img, (80, 80))
target3_img = pygame.transform.scale(target3_img, (80, 80))
target4_img = pygame.transform.scale(target4_img, (80, 80))
bam_img = pygame.transform.scale(bam_img, (80, 80))

target = random.choice([target1_img, target2_img, target3_img, target4_img])

target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

running = True
explosion_time = None
target_exploded = False
explosion_x = None
explosion_y = None

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                explosion_time = time.time()
                target_exploded = True
                explosion_x, explosion_y = target_x, target_y
                target = random.choice([target1_img, target2_img, target3_img, target4_img])
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)


    if target_exploded and explosion_time and time.time() - explosion_time < 0.5:
        screen.blit(bam_img, (explosion_x, explosion_y))
    else:
        screen.blit(target, (target_x, target_y))
        target_exploded = False

    pygame.display.update()

pygame.quit()
