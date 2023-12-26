#from map import load_map
import pygame, sys
import csv
import numpy as np
from character_class.main_character import Player as player
from ui.user_interface import UserInterface
from effects.effects_class import mouseEvents

#twoDArray = []
twoDArr = []
with open('map/alpha_map.csv', newline='') as file:
    twoDArr = np.array(list(csv.reader(file)))

print(twoDArr)
pygame.init()
screen = pygame.display.set_mode((1024, 720))
sizeTouple = screen.get_rect(topleft=(0,0))

def createSprite(name,fileName,position,width=0, height=0):

    name = pygame.sprite.Sprite()
    # if filename == "player.png":
    #     name.image = pygame.image.load(f'')
    # else:
    name.image = pygame.image.load(f'{fileName}.png').convert_alpha()
    name.rect = name.image.get_rect(topleft=position)
    
    if width and height:
        name.image = pygame.transform.scale(name.image,(width,height))

    return  name

water = createSprite("water","./images/water_tile",(0,0),64,64)
ground = createSprite("ground","./images/ground_tile",(0,0),64,64)


def cut_piece_from_TwoD_Arr(coordTuple, map_data, renderedSize):
    if coordTuple[0] <= 0:
        width = 0    
    else:
        width = coordTuple[0]
    if coordTuple[1] <= 0:
        height  = 0
    else:
        height = coordTuple[1]

    current_row = height // 18
    current_column = width // 32

    return map_data[current_row: current_row + renderedSize,
                     current_column: current_column + renderedSize]


visibleArr = cut_piece_from_TwoD_Arr(screen.get_rect().topleft, twoDArr, 20)   
           

bg_tiles_Group = pygame.sprite.Group()

def display_bg_tiles(x=0,y=0,tilesize=64):
    print(screen.get_rect().midtop)
    start_x =screen.get_rect().midtop[0]
    start_y = screen.get_rect().midtop[1]
    rowNum = start_x
    columnNum = start_y
    row = 1
    column = 1
    for rows in visibleArr:
        for element in rows:
            screen.blit(ground.image,(rowNum,columnNum))
            bg_tiles_Group.add(createSprite("water","./images/water_tile",(rowNum,columnNum),64,64))
            rowNum -= tilesize/2### Move to the left
            columnNum += tilesize/4 ### Move to the bottom
            print(row)

        
        #add new line start coordinates
        rowNum = start_x +((tilesize/2)*row)
        columnNum =  start_y+ ((tilesize/4)*column)
        column += 1
        row += 1

        ###

display_bg_tiles()
        ###
# player = createSprite("player",
#                       "demo/graphics/player",
#                       (screen.get_size()[0] // 2,
#                       screen.get_size()[1] // 2),32,32)

#     keys = pygame.key.get_pressed()
# def input(player):
#     direction = pygame.math.Vector2
#     direction.x, direction.y = 0,0

#     down = keys[pygame.K_DOWN]
#     up = keys[pygame.K_UP]
#     left = keys[pygame.K_LEFT]
#     right = keys[pygame.K_RIGHT]
#     if up:
     
#         direction.y = -1
#     elif down:
#         direction.y = 1
#     elif not up and not down and speed > 0.1 and (left or right):
#         direction.y = 0  
                    
#     if right:
#         direction.x = 1
#     elif left:
#         direction.x = -1
#     elif not right and not left and speed > 0.1 and (up or down):
#         direction.x = 0
        
#     if not up and not down and not right and not left:
#         speed /= 1.3
#         if speed <= 0.1:
#             direction.x = 0
#             direction.y = 0
           
            
# def input(event):
#         keys = pygame.key.get_pressed()
#         up = keys[pygame.K_UP]
#         down = keys[pygame.K_DOWN]
#         right = keys[pygame.K_RIGHT]
#         left = keys[pygame.K_LEFT]
         
#         if up:
#             direction.y = -1
#         elif down:
#             direction.y = 1
#         elif not up and not down and speed > 0.1 and (left or right):
#             direction.y = 0  
                        
#         if right:
#             direction.x = 1
#         elif left:
#             direction.x = -1
#         elif not right and not left and speed > 0.1 and (up or down):
#             direction.x = 0
            
#         if not up and not down and not right and not left:
#             speed /= 1.3
#             if speed <= 0.1:
#                 direction.x = 0
#                 direction.y = 0
            
# def update:
#         #input()
        
#         speed += acceleration
#         speed = min(speed, max_speed)
        
#         if direction.x and not direction.y:
#             rect.center += direction * speed
#         elif direction.y and not direction.x:
#             rect.center += direction * speed
#         elif direction.y and direction.x:
#             rect.center += (direction / 1.5) * speed

'''
ARRR[1:4, 1:4]

'''

ui =  UserInterface(screen)
#camera_group = camera_group()
#player = player((screen.get_size()[0] // 2, screen.get_size()[0] // 2), camera_group)

clock = pygame.time.Clock()



        
running = True
mesh_toggle = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                if mesh_toggle == False:
                    mesh_toggle = True
                    pygame.time.delay(100)
                else:
                    mesh_toggle = False
                    pygame.time.delay(100)
                    
            # if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
            #     camera_group.zoom_level += 0.1
            #     pygame.time.delay(30)
            # elif event.key == pygame.K_MINUS:
            #     camera_group.zoom_level -= 0.1
            #     pygame.time.delay(30)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseEvents(ui)


    screen.fill((0,0,0))
    #display_bg_tiles()
   # screen.blit(player.image,player.rect)
    #ui.display_ui()
    pygame.display.update()
    clock.tick(60)



