import pygame

class Water(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.surf = pygame.image.load('../demo/graphics/water_tile.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (100,100))
        self.rect = self.surf.get_rect(topleft=pos)
        self.surf.set_colorkey((0,0,0))