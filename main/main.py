import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900,900),0,32)
display = pygame.Surface((15000,15000))

water_img = pygame.image.load('.\water_tile.png').convert()
water_img.set_colorkey((0,0,0))

while True:
    display.fill((0,0,0))
    x = 7500
    y = 100
    y_value= y
    x_value = x
    map_size =40
    y_move_total = 120 *map_size
    for y_value in range(100, y_move_total , 120):
        for x_value in range(x, -1, -205):
        #for _ in range(map_size):
                display.blit(water_img, (x_value,y_value))
                x_value -= 205
                y_value+=120

        y +=y_value+120
        x += 205
       # print(value)

    #display.blit(water_img, (x,y))
    #display.blit(water_img, (x-205,y+120))
    # display.blit(water_img, (x-205-205,y+120+120))
    # display.blit(water_img, (150+205,100+117))
    # display.blit(water_img, (150+205+205,100+117+117))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (1,0))
    pygame.display.update()