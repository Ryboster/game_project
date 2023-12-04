from player import Player
import pygame
import sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')


screen = pygame.display.set_mode((900,900))

clock = pygame.time.Clock()
       


surface_size=(600,600)
sS = surface_size

display = pygame.Surface((sS[0],sS[1]))

water_img = pygame.image.load('./tilesets/water_64.png').convert()
land_img = pygame.image.load('./tilesets/land_64.png').convert()
fly_img = pygame.image.load('./demo/graphics/Fly/Fly1.png').convert()



fly_img.set_colorkey((255,255,255))
water_img.set_colorkey((0,0,0))
land_img.set_colorkey((0,0,0))
Two_D_array = [["Water", "Water", "Water", "Water","Water","Water"],
["Water", "Land", "Land", "Land", "Land","Water","Water"],
["Water", "Land", "Land", "Land", "Land","Water","Water"],
["Water", "Land", "Land", "Land", "Land","Land","Water"],
["Water", "Land", "Land", "Land","Land", "Land","Water"],
["Water", "Land", "Land", "Land","Land", "Land","Water"],
["Water", "Land", "Land", "Land", "Land","Land","Water"],
["Water", "Land", "Land", "Land","Land", "Water","Water"],
["Water", "Land", "Land", "Land","Land", "Water","Water"],
["Water", "Water", "Land", "Water","Water","Water"],]


def display_w(x,y):
    display.blit(water_img, (x,y))

def display_l(x,y):
    display.blit(land_img, (x,y))
test_x= 0
test_y= 0
function_mapping = {'Water': display_w, 'Land': display_l}
player = Player()
#from tutorial
RECTANGLE_COLOR_1 = (255, 0, 0)
RECTANGLE_COLOR_2 = (0, 0, 255)
rectangle_1 = pygame.Rect(200, 200, 100, 100)
rectangle_2 = pygame.Rect(500, 300, 150, 50)
camera_offset_x = 0


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
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            test_x +=1
        elif event.key == pygame.K_RIGHT:
            test_x  -=1
        elif event.key == pygame.K_UP:
            test_y +=1
        elif event.key == pygame.K_DOWN:
            test_y -=1
   # display.blit(fly_img, (300, 300))


    screen.blit(pygame.transform.scale(display, screen.get_size()), ((test_x , test_y)))
    # pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1)
    # pygame.draw.rect(screen, RECTANGLE_COLOR_2, rectangle_2)
    rectangle_1_draw_pos = rectangle_1.move(camera_offset_x, 0)
    pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1_draw_pos)
    
    # rectangle_2_draw_pos = rectangle_2.move(camera_offset_x, 0)
    # pygame.draw.rect(fly_img, RECTANGLE_COLOR_2, rectangle_2_draw_pos)
   
   # camera_group.custom_draw(player)
    #camera_group.update()
    pygame.display.update()
    #clock.tick(60)