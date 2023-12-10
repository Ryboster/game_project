import pygame

class CameraGroup(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        # Get display surface
        self.display_surf = pygame.display.get_surface()


        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        self.screen_size = self.display_surf.get_size()

        # Camera Rect
        self.camera_rect = pygame.Rect(self.offset.x, self.offset.y, self.screen_size[0], self.screen_size[1])
        
        from tile_classes.water import Water


    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
        
    def set_layers(self):
        for sprite in self.sprites():
            if isinstance(sprite, Water):
                sprite.layer = 1
        
    def ysort(self, player):
        self.center_target(player)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            if not isinstance(sprite, type(player)) and self.camera_rect.colliderect(sprite.rect):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surf.blit(sprite.surf, offset_pos)
                
            
        self.display_surf.blit(player.surf, player.rect.topleft - self.offset)

        # Camera Rect
        self.camera_rect = pygame.Rect(self.offset.x, self.offset.y, self.screen_size[0], self.screen_size[1])
        #self.display_surf.blit(player.surf, player.rect)
        
