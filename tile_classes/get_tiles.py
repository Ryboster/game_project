import csv
import pygame
#from ..tile_classes.water import Water
#from ..main import Water

class Load:
    def __init__(self):
        pass
    
        from .water import Water

        self.map_dict = {
            'W': Water,
        }
        
                        
    def load(self, camera_group):
        x = -128
        y = -64
        iters = 0
        #image = pygame.load.image('water_border.png')
        sprites_list = []
        with open('map/alpha_map.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for current_tile in row:
                    if current_tile == 'W':
                        tile = self.map_dict[current_tile]((x, y), camera_group)
                        sprites_list.append(tile)
                        #camera_group.change_layer(tile, 0)
                    x += 64
                if iters % 2 == 0:
                    x = -32
                    y += 18
                else:
                    x = -64
                    y += 18
                iters += 1
                                
        return sprites_list
