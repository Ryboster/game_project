### render_concept.py
from map import load_map
import pygame, sys
import csv
from player import Player as player
from map.load_map import Water
from camera_group import CameraGroup as camera_group


pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect(topleft=(0,0))

clock = pygame.time.Clock()


camera_group = camera_group()
player = player((screen.get_size()[0] // 2, screen.get_size()[0] // 2), camera_group)

x = 0
y = 0
iters = 0
from map.load_map import Load
Load(camera_group)
#camera_group.change_layer(player, 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    screen.fill((0,0,0))
    camera_group.update() 
    camera_group.custom_draw(player, Water)
    pygame.display.flip()
    clock.tick(60)
            