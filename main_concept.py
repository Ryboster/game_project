# from map import load_map
import pygame, sys
import csv
import numpy as np
import math
from character_class.main_character import Player as player
from ui.user_interface import UserInterface
from effects.effects_class import mouseEvents

twoDArr = []
with open("map/alpha_map.csv", newline="") as file:
    twoDArr = np.array(list(csv.reader(file)), dtype=str)

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


water = createSprite("water", "./images/water_tile", (0, 0),128,128)
ground = createSprite("ground", "./images/ground_tile", (0, 0), 128, 128)
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


visibleArr = cut_piece_from_TwoD_Arr(screen.get_rect().topleft, twoDArr, 30)


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
def blit_tile_relying_on_letter(letter,x,y):
    if letter == 'L':
        return screen.blit(ground.image, (x,y))
    else:
        return screen.blit(water.image, (x,y))

def quicker_set_bg_tiles(x=0,y=0,tilesize=128):
    start_x = screen.get_rect().midtop[0] + x
    start_y = screen.get_rect().midtop[1] + y
    value_x = start_x
    value_y = start_y

    for index, element in np.ndenumerate(visibleArr):
        #x coordinate equals starting point minus half of tile width 
        #and the half of the width is multipled
        #by the column number counting from 0
        #to adjust next lines half of tile width is added to x coordinate, multiplied by row number couting from 0
        value_x = start_x - (tilesize // 2) - (index[0] * (tilesize // 2)) + (index[1] * (tilesize // 2))
        value_y = start_y + (tilesize // 4) + (index[0] * (tilesize // 4)) + (index[1] * (tilesize // 4))
        blit_tile_relying_on_letter(element,value_x, value_y)
        #screen.blit(ground.image, (value_x,value_y))

quicker_set_bg_tiles()

class plyer_movement():
    def __init__(self):
        super().__init__()
        self.coordinates_x = 0
        self.coordinates_y = 0
    
    def player_movement(self,keys):
        if keys[pygame.K_UP]:
            self.coordinates_y += 5
        elif keys[pygame.K_DOWN]:
            self.coordinates_y -= 5
        elif keys[pygame.K_RIGHT]:
            self.coordinates_x -= 5
        elif keys[pygame.K_LEFT]:
            self.coordinates_x += 5


newPlayer = plyer_movement()
ui = UserInterface(screen)
clock = pygame.time.Clock()

#while(1) imprive speed by couple miliseconds coparing with true
running = 1
mesh_toggle = False
def create_isometric_coordinates(cartesian_x, cartesian_y):
    xtest= cartesian_x * -1
    ytest=(cartesian_y-(screen.get_size()[1] // 2)) * -1
    coordx=  (2*ytest+xtest)//(ground.image.get_rect().width )
    coordy= (2*ytest-xtest)//(ground.image.get_rect().width )
    return (coordx,coordy)
while running:
    #this should limit allowed events to read  
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

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
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseEvents(ui)
    keys = pygame.key.get_pressed()
    newPlayer.player_movement(keys)

    screen.fill((0, 0, 255))
    
    print("x and y coord",create_isometric_coordinates(newPlayer.coordinates_x,newPlayer.coordinates_y))

    quicker_set_bg_tiles(newPlayer.coordinates_x, (newPlayer.coordinates_y))

    bg_tiles_Group.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(60)
