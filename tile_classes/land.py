import pygame

class Water(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.surf = pygame.image.load('images/land64.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (64,64))
        self.rect = self.surf.get_rect(topleft=pos)
        self.surf.set_colorkey((0,0,0))