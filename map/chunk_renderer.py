from PIL import Image
import csv
from random import randint
import sys

class Chunk:
    def __init__(self, f: int, l: int, data: list):
        self.name = f'{f},{l}'
        self.chunk_data = data


class RenderChunks:
    def __init__(self):
        #1280 748
        #1280 723
        
        self.CHUNK_SIZE = (1280, 723)
        self.TILE_SIZE = (64, 64)
        self.CURRENT_CHUNK = 0
        self.max_tile = {
            'x': 0,
            'y': 0
        }
        
    ''' Get chunk size in main script '''
    def get_chunk_size(self):
        return self.CHUNK_SIZE
        
    ''' Status bar '''
    ### Prints out status bar updates while rendering
    def print_status_bar(self, iteration, total, length= 50, prefix='', fill = '█'):
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write('\r%s |%s| %s%s %s' % (prefix ,bar, percent, '%', 'Completed'))
        
    ''' get maximum number of chunks per map '''
    def get_chunk_num(self, map_data):   
        chunks_vert, chunks_hor = 0, 0
             
        for k in range(0, len(map_data), self.max_tile['y']):
            chunks_vert += 1
        for i in range(0, len(map_data[0]), self.max_tile['x']):
            chunks_hor += 1
        return (int(chunks_hor),  int(chunks_vert))

            
    ''' get maximum number of tiles per chunk'''
    ### Both dimensions have to be equal
    def get_max_tiles(self):        
        
        for i in range(0, self.CHUNK_SIZE[0] // 2, 32):
            self.max_tile['x'] += 1
            
        for i in range(0, (self.CHUNK_SIZE[0] // 2), 32):
            self.max_tile['y'] += 1
                           
    ''' split the csv into lists the size of the chunk '''
    ### Chunks are initialized with only a part of the map
    def partition_csv(self, map_data):
        max_chunks = self.get_chunk_num(map_data)
        buffer = []
        chunk = []
        chunks = []
        name_x = 0
        name_y = 0
        while map_data:
            if not map_data[0]:
                map_data.pop(0)
                if not map_data:
                    break                
            else:
                for i in range(0, self.max_tile['y']):
                    for k in range(0, self.max_tile['x']):
                        try:
                            if map_data[i][0]:
                                buffer.append(map_data[i][0])
                                map_data[i].pop(0)
                        except IndexError:
                            break
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
                
        return chunks
    
    
    ''' Increment position with each tile '''
    def increment_coordinates(self,x,y):
        y += 18
        x -= 32
        
        return x, y
    
    
    ''' Get starting position for current row '''
    def get_start_row_pos(self, count):
        ### Block dimensions
        block_height = self.TILE_SIZE[1]
        block_width = self.TILE_SIZE[0]
        
        ### Distance from another tile
        height_decr = -18
        width_incr = 32
        height_incr = 18
        
        ### Starting position increment
        starting_x = self.CHUNK_SIZE[0] // 2 + (block_width//2 * count)
        starting_y = 0 + (height_incr * count) 
    
        #starting_x = width_incr * self.max_tile['x'] + (block_width//2 * count)
        #starting_y = height_decr * self.max_tile['y'] + (18 * count)
        
        return starting_x, starting_y
        
    
    ''' Render chunk as png '''
    def create_png(self, map_data, name):
        
        self.expected_chunk_size = ()
        
        tile_images = {
        'W': 'tile_images/water_tile.png',
        'L': 'tile_images/ground_tile.png'
        }                      
                  
        result_image = Image.new('RGBA', self.CHUNK_SIZE, (0,0,0,0))
        
        ''' Starting coordinates must be top-right '''
        for count, row in enumerate(map_data):
            
            x, y = self.get_start_row_pos(count)
        
            for cc, col in reversed(list(enumerate(row))):
                
                image_path = tile_images[col]
                tile_image = Image.open(image_path)
                tile_image = tile_image.resize(self.TILE_SIZE)

                result_image.paste(tile_image, (x, y), tile_image)
                x,y = self.increment_coordinates(x,y)
            
        result_image.convert('RGBA')
        result_image.save(f'chunk_temp/{name}.png')

        img = Image.open(f'chunk_temp/{name}.png')
        trimmed_img = Image.alpha_composite(Image.new("RGBA", img.size, (0,0,0,0)), img).convert('RGB')
        bbox = trimmed_img.getbbox()
        cropped_img = img.crop(bbox)
        
        width, height = cropped_img.size
        if (width, height) < self.CHUNK_SIZE or (width, height) > self.CHUNK_SIZE:
            width,height = self.CHUNK_SIZE
        
        final_image = Image.new("RGBA", (width, height), (0,0,0,0))
        final_image.paste(cropped_img,(0,0))
        final_image.save(f'chunk_temp/{name}.png')
        

### Class for initializing chunks with their respective positions. Called in main.
class GetChunks:
    def __init__(self):
        self.chunk_size = RenderChunks().get_chunk_size()
    
    
    def get_starting_col_pos(self,x,y,count):

        print('count:',count)
        x = 0 + int((self.chunk_size[0] // 2) * count)
        y = 0 - int((self.chunk_size[1] // 2) * count)
        return x,y

    ''' Load in chunks ''' ### Temporary Solution
    def get_chunk_list(self, ordered_names, camera_group):
        
        from tile_classes.tempchunk import TempChunk
        chunks = []

        pos = [0, 0]
        ctrl = [0,0]

        for count, surf_name in enumerate(ordered_names):
            
            comparison_var = [int(surf_name[0]), int(surf_name[2])]
            chunk = TempChunk(tuple((pos[0], pos[1])), camera_group, surf_name)
            chunks.append(chunk)    
            print('-' * 20, '\nCHUNKED!\n', f'\nNAME: {surf_name}\n', f'\nPOSITION: {pos}\n','-' *20)
                
            try:
                if ctrl[0] != int(ordered_names[count+1][0]):
                    ctrl[0] += 1
                    ctrl[1] = 0
                    print('ctrl0:',ctrl[0])
                    pos[0], pos[1] = self.get_starting_col_pos(pos[0], pos[1], ctrl[0])
                    
                    
                else:
                    pos[1] += (self.chunk_size[1] //2)
                    pos[0] += (self.chunk_size[0] //2)
                    ctrl[1] +=1
                    
            except IndexError:
                print(IndexError)
                break
        return chunks

        

### Ignore if imported.
if __name__ == "__main__":
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
        render.print_status_bar(count, len(chunks) - 1, length=50, prefix = f'\nGenerating chunk {count + 1} out of {len(chunks)}\n')
        render.create_png(chunk.chunk_data, chunk.name)
        
    print('finished')