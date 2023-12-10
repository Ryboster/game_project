import os

def find_chunks():
    images = 'map/chunk_temp/'
    chunk_list = []
    if os.path.exists(images) and os.path.isdir(images):
        for filename in os.listdir(images):
            if filename.endswith('.png'):
                print(filename.split('.'))
                chunk_list.append(filename.split('.')[0])
    
    return chunk_list