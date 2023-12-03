import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900,900),0,32)

surface_size=(500,500)
sS = surface_size

display = pygame.Surface((sS[0],sS[1]))

water_img = pygame.image.load('./tilesets/water_64.png').convert()
land_img = pygame.image.load('./tilesets/land_64.png').convert()

water_img.set_colorkey((0,0,0))
land_img.set_colorkey((0,0,0))
Two_D_array = [["Water", "Water", "Water", "Water","Water","Water"],
["Water", "Land", "Land", "Land", "Water","Water"],
["Water", "Land", "Land", "Land", "Water","Water"],
["Water", "Land", "Land", "Land", "Land","Water"],
["Water", "Land", "Land", "Land", "Land","Water"],
["Water", "Land", "Land", "Land", "Land","Water"],
["Water", "Land", "Land", "Land", "Water","Water"],
["Water", "Land", "Land", "Land", "Water","Water"],
["Water", "Water", "Land", "Water","Water","Water"],]


def display_w(x,y):
    display.blit(water_img, (x,y))

def display_l(x,y):
    display.blit(land_img, (x,y))

function_mapping = {'Water': display_w, 'Land': display_l}


while True:
    display.fill((0,0,0))
    x = sS[0]//3
    y = 10
    temp_x = x
    temp_y = y
    current_x_lvl = x
    current_y_lvl = y
    for row in Two_D_array: 
        for element in row:
            function_mapping[element](temp_x,temp_y)
            #display.blit(water_img, (temp_x,temp_y))
            temp_x-=32
            temp_y+=16
        current_x_lvl += 32
        current_y_lvl += 16
        temp_x =  current_x_lvl
        temp_y =   current_y_lvl

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