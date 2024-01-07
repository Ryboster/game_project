# from map import load_map
import pygame, sys
import csv
import numpy as np
import math
from character_class.main_character import Player as player
from ui.user_interface import UserInterface
from effects.effects_class import mouseEvents

pygame.init()
screen = pygame.display.set_mode((1024, 720))
sizeTouple = screen.get_rect(topleft=(0, 0))

class CameraGroup():
    def __init__(self):
        #super().__init__()
        # Get display surface
        self.display_surf = pygame.display.get_surface()


        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        self.screen_size = self.display_surf.get_size()

        # Camera Rect
        self.camera_rect = pygame.Rect(self.offset.x, self.offset.y, self.screen_size[0], self.screen_size[1])
        

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center

    def quicker_set_bg_tiles(self, x=0,y=0,tilesize=128):
        start_x = (screen.get_size()[0] // 2)-64 + x
        #screen.get_rect().midtop[0] + x
        start_y = -64 + y
        #screen.get_rect().midtop[1] + y
        value_x = start_x
        value_y = start_y

        for index, element in np.ndenumerate(visibleArr):
            #x coordinate equals starting point minus half of tile width 
            #and the half of the width is multipled
            #by the column number counting from 0
            #to adjust next lines half of tile width is added to x coordinate, multiplied by row number couting from 0
            value_x = start_x - (tilesize // 2) - (index[0] * (tilesize // 2)) + (index[1] * (tilesize // 2))
            value_y = start_y + (tilesize // 4) + (index[0] * (tilesize // 4)) + (index[1] * (tilesize // 4))
            #print('blitting at: ', value_x, value_y)
            


            blit_tile_relying_on_letter(element,value_x, value_y,index)

        
    def display_on_screen(self, player):
        
        # Center player
        self.center_target(player)
             
        self.display_surf.blit(player.image, player.rect.topleft - self.offset)



camera = CameraGroup()


twoDArr = []
with open("map/alpha_map.csv", newline="") as file:
    twoDArr = np.array(list(csv.reader(file)), dtype=str)




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


### Replaced function. It now takes isometric coordinates instead of game coordinates.
def cut_piece_from_TwoD_Arr(coords, map_data, size):
    coords_x = coords[0]
    coords_y = coords[1]
    start_row = coords_x
    end_row= coords_y
    start_column=  coords_x +size 
    end_column= coords_y+ size 
    # # if visible area for the left side of the player do not fall behind array length
    # # set start row half the lenght of the visible size from the player
    # # otherwise set start row to 0
    # if coords_x - (size // 2) >= 0:      
    #     start_row = coords_x - size 
    # else:
    #     start_row = 1
    #     start_column =size
        
    # if coords_y - (size // 2) >= 0:
    #     start_column = coords_y - (size // 2)
    # else:
    #    end_row = 0
    #    #start_column = 0
    #    end_column = size
    #arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    #testarr = np.array([[ 0,  1,  2,  3],[ 4  ,5,  6,  7],[ 8,  9, 10, 11],[12, 13, 14, 15],[16, 17 ,18, 19],[20, 21, 22, 23]])
    '''debugging prints:'''    
    print(coords,size)
    print(map_data[start_row:start_column, end_row:end_column])
    # print(map_data[
    #     start_row: start_column,
    #     end_row: end_column,
    # ])
    # return map_data[
    #     start_row: start_column,
    #     end_row: end_column,
    # ]
    return map_data[start_row:start_column, end_row:end_column]


visibleArr = cut_piece_from_TwoD_Arr((0,0), twoDArr, 6)


def blit_tile_relying_on_letter(letter,x,y, index):
    font = pygame.font.Font("./fonts/Arial_Bold.ttf", 16)
    text = font.render(f"{(index[0], index[1])}", True, 'black')
    textRect = text.get_rect()

    if letter == 'L':
        screen.blit(ground.image, (x,y))
    else:
        screen.blit(water.image, (x,y))

    screen.blit(text, (x,y))
    return


# Broken at the moment - Wrong coordinates - Things are being blitted outside of visible area.


#quicker_set_bg_tiles()

class plyer_movement():
    def __init__(self):
        super().__init__()
        self.coordinates_x = 0
        self.coordinates_y = 0
        self.isometric_position_x = 0
        self.isometric_position_y = 0
    def player_movement(self,keys):
        if keys[pygame.K_UP]:
            self.coordinates_y += 4
            self.isometric_position_y +=4
        elif keys[pygame.K_DOWN]:
            self.coordinates_y -= 4
            self.isometric_position_y -= 4
        elif keys[pygame.K_RIGHT]:
            self.coordinates_x += 4
            self.isometric_position_x -= 4
        elif keys[pygame.K_LEFT]:
            self.coordinates_x -= 4
            self.isometric_position_x += 4


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

current_player_pos = (0,0)

while running:
    
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

    if current_player_pos != create_isometric_coordinates(newPlayer.coordinates_x,newPlayer.coordinates_y):
        current_player_pos = create_isometric_coordinates(newPlayer.coordinates_x,newPlayer.coordinates_y)
        visibleArr = cut_piece_from_TwoD_Arr(current_player_pos, twoDArr, 12)
        #newPlayer.coordinates_x = screen.get_size()[1] // 2
        #newPlayer.coordinates_y = screen.get_size()[0] // 2
        newPlayer.isometric_position_x= 64 -4
        newPlayer.isometric_position_y =32 +4
        #restarty =  (newPlayer.coordinates_y+ screen.get_size()[1] // 2)
    # #this should limit allowed events to read  
    # else:
    print('player iso',newPlayer.isometric_position_x, newPlayer.isometric_position_y)
    camera.quicker_set_bg_tiles(newPlayer.isometric_position_x,newPlayer.isometric_position_y)

    camera.display_on_screen(player)
    #screen.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(60)