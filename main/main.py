import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900,900),0,32)
display = pygame.Surface((300,300))

water_img = pygame.image.load('water_tile.png').convert()
water_img.set_colorkey((0,0,0))

while True:
    display.fill((0,0,0))

    display.blit(water_img, (150,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
    pygame.display.update()