#from map import load_map
import pygame, sys
import csv
from character_class.main_character import Player as player
from tile_classes.water import Water
from camera_group import CameraGroup as camera_group
from map.get_chunks import find_chunks
from tile_classes.get_tiles import Load
from ui.user_interface import UserInterface
from tile_classes.tempchunk import TempChunk
from effects.effects_class import mouseEvents
from map.chunk_renderer import RenderChunks, GetChunks


pygame.init()

screen = pygame.display.set_mode((1024, 720))
screen_rect = screen.get_rect(topleft=(0,0))

ui =  UserInterface(screen)
camera_group = camera_group()
player = player((0,0), camera_group)

  
''' Order chunks by name '''
ordered_names = [x for x in sorted(find_chunks(), key= lambda surf_name: tuple((int(surf_name[0]), int(surf_name[2]))))]

screen_dims = screen.get_size()
chunk_size = RenderChunks().get_chunk_size()

chunks = GetChunks().get_chunk_list(ordered_names, camera_group)
 
clock = pygame.time.Clock()

#Load().compile()

tiles = Load().load()
camera_group.all_objects = tiles
camera_group.all_chunks = chunks

        
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
                    
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                camera_group.zoom_level += 0.1
                pygame.time.delay(30)
            elif event.key == pygame.K_MINUS:
                camera_group.zoom_level -= 0.1
                pygame.time.delay(30)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseEvents(ui)


    screen.fill((0,0,0))
    
    camera_group.ysort(player, mesh_toggle)
    camera_group.update()
    ui.display_ui()
    pygame.display.update()
    clock.tick(60)