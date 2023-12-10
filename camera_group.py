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
        

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
        
    def set_layers(self):
        
        from tile_classes.water import Water
        from main import TempChunk
        from character_class.main_character import Player
        
        self.Water = Water
        self.TempChunk = TempChunk
        self.Player = Player
        
        for sprite in self.sprites():
            if isinstance(sprite, Water):
                self.change_layer(sprite, 1)
            if isinstance(sprite, TempChunk):
                self.change_layer(sprite, 0)
            if isinstance(sprite, Player):
                self.change_layer(sprite, 2)
        
    def ysort(self, player, net_toggle):
        
        self.center_target(player)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.layer):
            
            if not net_toggle:
                if isinstance(sprite, self.Water):
                    continue
            
            if self.camera_rect.colliderect(sprite.rect):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surf.blit(sprite.surf, offset_pos)