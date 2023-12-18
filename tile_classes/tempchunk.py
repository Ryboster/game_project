import pygame


''' Temporary Chunk Class '''
class TempChunk(pygame.sprite.Sprite):
    def __init__(self, pos, group, surf_name):
        super().__init__(group)
        self.pos = pos
        self.surf = pygame.image.load(f'map/chunk_temp/{surf_name}.png')
        self.rect = self.surf.get_rect(topleft=pos)