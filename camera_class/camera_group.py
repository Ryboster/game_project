import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init()
        # Get display surface
        self.display_surf = pygame.display.get_surface()


        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        self.screen_size = self.display_surf.get_size()

        # Camera Rect
        self.camera_rect = pygame.Rect(self.offset.x, self.offset.y, self.screen_size[0], self.screen_size[1])

        # Zoom variable
        self.zoom_level = 1.0 
        
    def center_target(self, target):
        # Recalculate offset
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        # Place camera_rect on player
        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
        
    def draw(self, player):
        
        # Check if zooming
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.zoom_level *= 1.1
        elif keys[pygame.K_DOWN]:
            self.zoom_level /= 1.1
        
        # Center camera around player    
        self.center_target(player)
        
        ## Y-Sort Camera
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = (sprite.rect.topleft * self.zoom_level) - self.offset
            self.display_surf.blit(sprite, offset_pos)
        
