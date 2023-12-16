import csv
import pygame
import pickle
from tile_classes.tile import Tile


class Load:
    def __init__(self):
        pass
        
    def compile(self):
        x = 0
        y = 0
        iters = 0
        tiles_list = []
        
        with open('map/alpha_map.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for current_tile in row:
                    tile = Tile((x,y),'W')
                    tiles_list.append(tile)
                    x += 64
                    
                if iters % 2 == 0:
                    x = -32
                    y += 18
                else:
                    x = -64
                    y += 18
                iters += 1
        
        with open('pre-compiled_tiles.pkl', 'wb') as file:
            pickle.dump(tiles_list, file)
                        
                        
    def load(self):
        all_tiles = {}
        with open('pre-compiled_tiles.pkl', 'rb') as tiles:
            tiles = pickle.load(tiles)
            for tile in tiles:
                all_tiles[tile.pos] = tile.id
            
        return all_tiles