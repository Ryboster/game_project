from PIL import Image
import csv
from random import randint

class Chunk():
    def __init__(self, f: int, l: int, data: list):
        self.name = f'{f},{l}'
        self.chunk_data = data


class RenderChunks():
    def __init__(self):
        self.CHUNK_SIZE = (1024, 720)
        self.TILE_SIZE = (64, 64)
        self.CURRENT_CHUNK = 0
        self.max_tile = {
            'x': 0,
            'y': 0
        }
        
    ''' get maximum number of chunks per map '''
    def get_chunk_num(self, map_data):   
        chunks_vert, chunks_hor = 0, 0
             
        for k in range(0, len(map_data), self.max_tile['y']):
            chunks_vert += 1
        for i in range(0, len(map_data[0]), self.max_tile['x']):
            chunks_hor += 1
            
        return (int(chunks_hor),  int(chunks_vert))

            
    ''' get maximum number of tiles per chunk'''
    def get_max_tiles(self):        
        for i in range(-64, self.CHUNK_SIZE[0], self.TILE_SIZE[0]):
            self.max_tile['x'] += 1
        for i in range(-64, self.CHUNK_SIZE[1], 18):
            self.max_tile['y'] += 1
            print(i)
                            
    ''' split the csv into lists the size of the chunk '''
    def partition_csv(self, map_data):
        
        max_chunks = self.get_chunk_num(map_data)
        buffer = []
        chunk = []
        chunks = []
        name_x = 0
        name_y = 0
        while map_data:
            
            y_incr = False
            
            if not map_data[0]:
                map_data.pop(0)
                if not map_data:
                    break                
            else:
                #print('MAP LENGTH: ', len(map_data))
                for i in range(0, self.max_tile['y']):
                    for k in range(0, self.max_tile['x']):
                        try:
                            if map_data[i][0]:
                                buffer.append(map_data[i][0])
                                map_data[i].pop(0)
                        except IndexError:
                            break
                        
                    #print(self.max_tile['y'])
                    
                    if buffer:
                        chunk.append(buffer.copy()) 
                        buffer.clear()
                        
                
                if name_x >= max_chunks[0]:
                    name_y +=1
                    name_x = 0
                
                new_chunk = Chunk(name_x, name_y, chunk.copy())
                chunk.clear()
                chunks.append(new_chunk)
                name_x += 1    
                #print(len(new_chunk.chunk_data))
                
        return chunks
    
    ''' Render chunk as png '''
    def create_png(self, map_data, name):
        
        tile_images = {
        'W': 'tile_images/water_tile.png',
        'L': 'tile_images/ground_tile.png'
        }                                
        result_image = Image.new('RGB', (self.CHUNK_SIZE[0], self.CHUNK_SIZE[1]), (0,0,0,0))
        
        x = -64
        y = -64

        for count, row in enumerate(map_data):
            for col in row:
                image_path = tile_images[col]
                tile_image = Image.open(image_path)
                tile_image = tile_image.resize(self.TILE_SIZE)
            
                result_image.paste(tile_image, (x, y), tile_image)
                    
                x+= 64
            
            if count %2 == 0:
                x = -32
                y += 18
            else:
                x = -64
                y += 18
            
        result_image.save(f'chunk_temp/{name}.png')


def read_csv(file_path):
    map_data = []
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            map_data.append([cell for cell in row])
    return map_data

map_data = read_csv('alpha_map.csv')


render = RenderChunks()
render.get_max_tiles()

chunks = render.partition_csv(map_data)

for count, chunk in enumerate(chunks):
    render.create_png(chunk.chunk_data, chunk.name)
    
print('finished')