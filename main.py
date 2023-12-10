#from map import load_map
import pygame, sys
import csv
from character_class.main_character import Player as player
from tile_classes.water import Water
from camera_group import CameraGroup as camera_group
from map.chunks import chunk_surfs
from tile_classes.get_tiles import Load

pygame.init()

screen = pygame.display.set_mode((1024, 720))
screen_rect = screen.get_rect(topleft=(0,0))

camera_group = camera_group()
player = player((screen.get_size()[0] // 2, screen.get_size()[0] // 2), camera_group)

''' Temporary Chunk Class '''
class TempChunk(pygame.sprite.Sprite):
    def __init__(self, pos, group, surf_name):
        super().__init__(group)
        self.surf = pygame.image.load(f'map/chunk_temp/{surf_name}.png')
        self.rect = self.surf.get_rect(topleft=pos)

       
''' Order chunks by name '''
ordered_names = [x for x in sorted(chunk_surfs(), key= lambda surf_name: tuple((int(surf_name[0]), int(surf_name[2]))))]

pos = [0, 0]
ctrl = [0,0]
screen_dims = screen.get_size()

''' Load in chunks ''' ### Temporary Solution
for count, surf_name in enumerate(ordered_names):
    
    comparison_var = [int(surf_name[0]), int(surf_name[2])]
    TempChunk(tuple((pos[0], pos[1])), camera_group, surf_name)
    print('-' * 20, '\nCHUNKED!\n', f'\nNAME: {surf_name}\n', f'\nPOSITION: {pos}\n','-' *20)
    
    try:
        if ctrl[0] != int(ordered_names[count+1][0]):
            pos[0] += screen_dims[0]
            pos[1] = 0
            ctrl[0] += 1
            ctrl[1] = 0
            
        else:
            pos[1] += screen_dims[1]
            ctrl[1] +=1
            
    except IndexError:
        break

 
 
clock = pygame.time.Clock()

Load().load(camera_group)
camera_group.set_layers()
        
running = True
mesh_toggle = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_F1]:        
            if mesh_toggle:
                mesh_toggle = False
            else:
                mesh_toggle = True
        
    
    screen.fill((0,0,0))
    camera_group.ysort(player, mesh_toggle)
    camera_group.update()
    pygame.display.update()
    