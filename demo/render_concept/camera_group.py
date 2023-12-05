### camera_group.py

import pygame
from pygame.sprite import LayeredUpdates

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        self.wh = self.display_surf.get_size()

        # Camera rect
        self.camera_rect = pygame.Rect(self.offset.x,self.offset.y, self.wh[0] +400, self.wh[1] +400)
        
        ### Zoom
        self.zoom_level = 1.0 
        
    def change_layer(self, sprite, new_layer):
        if sprite in self:
            self.remove(sprite)
            sprite.layer = new_layer
            self.add(sprite, layer=new_layer)

    def update(self):
        for sprite in self.sprites():
            sprite.update()
    
    def box_camera(self,target):
        
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
        
    def custom_draw(self, player, Water):
        
        ### Zoom 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
            self.zoom_level *= 1.2
            
        elif keys[pygame.K_MINUS]:
            self.zoom_level /= 1.2

        
        # Box camera
        self.box_camera(player)
        
        # Y-Sort Camera
        for tile in sorted(self.sprites(), key=lambda tile: tile.rect.centery):
            if not self.camera_rect.colliderect(tile.rect):
                continue
            if not isinstance(tile, type(player)):
                if not hasattr(tile, 'original_surf'):
                    tile.original_surf = tile.surf.copy()
                    
                width, height = tile.original_surf.get_size()
                scaled_width = int(width / self.zoom_level)
                scaled_height = int(height / self.zoom_level)
                
                tile.surf = pygame.transform.scale(tile.original_surf,(scaled_width, scaled_height))
        
                offset_pos = tile.rect.topleft - self.offset
                self.display_surf.blit(tile.surf, offset_pos)
            
        player_offset_pos = player.rect.topleft - self.offset
        self.display_surf.blit(player.surf, player_offset_pos)
        
        #pygame.draw.rect(self.display_surf, 'yellow', player.rect, 5)
        #print(self.camera_rect.center)
        #self.display_surf.blit(player.surf, player.rect)