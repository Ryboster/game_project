# from map import load_map
import pygame, sys
import csv
import numpy as np
from character_class.main_character import Player as player
from ui.user_interface import UserInterface
from effects.effects_class import mouseEvents

twoDArr = []
with open("map/alpha_map.csv", newline="") as file:
    twoDArr = np.array(list(csv.reader(file)))

#print(twoDArr)
pygame.init()
screen = pygame.display.set_mode((1024, 720))
sizeTouple = screen.get_rect(topleft=(0, 0))


def createSprite(name, fileName, position, width=0, height=0):
    name = pygame.sprite.Sprite()
    name.image = pygame.image.load(f"{fileName}.png").convert_alpha()
    name.rect = name.image.get_rect(topleft=position)

    if width and height:
        name.image = pygame.transform.scale(name.image, (width, height))

    return name


water = createSprite("water", "./images/water_tile", (0, 0))
ground = createSprite("ground", "./images/ground_tile", (0, 0), 64, 64)
player = createSprite(
    "player",
    "./images/player",
    (screen.get_size()[0] // 2, screen.get_size()[1] // 2),
    32,
    32,
)


def cut_piece_from_TwoD_Arr(coordTuple, map_data, renderedSize):
    if coordTuple[0] <= 0:
        width = 0
    else:
        width = coordTuple[0]
    if coordTuple[1] <= 0:
        height = 0
    else:
        height = coordTuple[1]

    current_row = height // 16
    current_column = width // 32

    return map_data[
        current_row : current_row + renderedSize,
        current_column : current_column + renderedSize,
    ]


visibleArr = cut_piece_from_TwoD_Arr(screen.get_rect().topleft, twoDArr, 16)


bg_tiles_Group = pygame.sprite.Group()


def set_bg_tiles(x=0, y=0, tilesize=64):
    bg_tiles_Group.empty()
    start_x = screen.get_rect().midtop[0] + x
    start_y = screen.get_rect().midtop[1] + y
    rowNum = start_x
    columnNum = start_y
    row = 1
    column = 1
    for rows in visibleArr:
        for element in rows:
            #screen.blit(ground.image, (rowNum, columnNum))
            bg_tiles_Group.add(
                createSprite("water", "./images/water_64", (rowNum, columnNum), tilesize, tilesize)
            )
            rowNum -= tilesize / 2  ### Move to the left
            columnNum += tilesize / 4  ### Move to the bottom
            print(row)
            #print(len(bg_tiles_Group))

        # add new line start coordinates
        rowNum = start_x + ((tilesize / 2) * row)
        columnNum = start_y + ((tilesize / 4) * column)
        column += 1
        row += 1

# def quicker_set_bg_tiles(x=0,y=0,tilesize=64):
#     bg_tiles_Group.empty()
#     start_x = screen.get_rect().midtop[0] + x
#     start_y = screen.get_rect().midtop[1] + y
#     value_x = start_x
#     value_y = start_y
#     ##
#     for index, element in np.ndenumerate(visibleArr):
#         bg_tiles_Group.add(
#                 createSprite("water", "./images/water_64", (value_x,value_y), tilesize, tilesize)
#             )
#         value_x -= (index[0] *(tilesize / 2) )
#         value_y += (index[1] *(tilesize / 4) )
#         print(index, element)

# quicker_set_bg_tiles()
#set_bg_tiles()


class playerTest():
    def __init__(self):
        super().__init__()
        self.movement_x = 0
        self.movement_y = 0
    
    def player_movement(self,event):
        if event.key == 119 or event.key == 1073741906:
            self.movement_y += 5
            #print("event type up",self.movement_y)
        elif event.key == 100 or event.key == 1073741903:
            self.movement_x -= 5
            #print("event type right")
        elif event.key == 115 or event.key == 1073741905:
            self.movement_y -= 5
            #print("event type down")
        elif event.key == 97 or event.key == 1073741904:
            self.movement_x += 5
            #print("event type left")

newPlayer = playerTest()


"""
ARRR[1:4, 1:4]

"""

ui = UserInterface(screen)
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
            #newPlayer.player_movement(event)
            #set_bg_tiles(newPlayer.movement_x, newPlayer.movement_y)
           # print(bg_tiles_Group.get_rect().topleft)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseEvents(ui)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        newPlayer.player_movement(event)
        quicker_set_bg_tiles()
        #set_bg_tiles(newPlayer.movement_x, newPlayer.movement_y)
    if keys[pygame.K_DOWN]:
        newPlayer.player_movement(event)
        quicker_set_bg_tiles()
        #set_bg_tiles(newPlayer.movement_x, newPlayer.movement_y)
    if keys[pygame.K_RIGHT]:
        newPlayer.player_movement(event)
        quicker_set_bg_tiles()
        #set_bg_tiles(newPlayer.movement_x, newPlayer.movement_y)
    if keys[pygame.K_LEFT]:
        newPlayer.player_movement(event)
        quicker_set_bg_tiles()
        #set_bg_tiles(newPlayer.movement_x, newPlayer.movement_y)


    screen.fill((0, 0, 255))
    bg_tiles_Group.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(30)
