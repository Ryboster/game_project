import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init()
        # Get display surface
        self.display_surf = pygame.display.get_surface()
        