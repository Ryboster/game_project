import pygame


''' Temporary Chunk Class '''
class TempChunk(pygame.sprite.Sprite):
    __slots__ = ["pos", "group", "surf_name"]
    def __init__(self, pos, group, surf_name):
        super().__init__(group)
        self.pos = pos
        self.surf = pygame.image.load(f'map/chunk_temp/{surf_name}.png')
        ### Changed placing due to new shape
        self.rect = self.surf.get_rect()
        self.rect.left = pos[0]
        self.rect.centery = pos[1]