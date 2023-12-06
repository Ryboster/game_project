import csv
import pygame


class Water(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.surf = pygame.image.load('graphics/water_tile.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100,100))
        self.rect = self.surf.get_rect(topleft=pos)
        self.surf.set_colorkey((0,0,0))

map_dict = {
    'w': Water
}

class Load:
    def __init__(self, camera_group):
        x = 0
        y = 0
        iters = 0
        with open('map/tiles.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for current_tile in row:
                    tile = map_dict[current_tile]((x, y), camera_group)
                    #camera_group.change_layer(tile, 0)
                    x += 100
                iters += 1
                if iters % 2 == 0:
                    x = 0
                    y += 30
                else:
                    x = 50
                    y += 30
                    
                    