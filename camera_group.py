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
        
        self.zoom_level = 1.0
        
        self.all_objects = []
        self.active_elements = {}
        
        self.all_chunks = []
        
        
        from tile_classes.water import Water
        from character_class.main_character import Player
        from tile_classes.tile import Tile
        from tile_classes.tempchunk import TempChunk

                
        self.Water = Water
        self.TempChunk = TempChunk
        self.Player = Player
        self.Tile = Tile
        
        self.map_dict = {
            'W': Water,
            'Temp': TempChunk,
            'P': Player
        }
        

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
                        
                        
    def get_active_elements(self, player):
        self.active_elements.clear()
         
        def get_expected(start_x, start_y):
            for x in range(start_x, player.rect.topright[0] + 32, 64):
                for y in range(start_y, player.rect.bottomright[1], 36):
                    if (x,y) not in self.all_objects:
                        pass
                    self.active_elements[(x,y)] = self.all_objects[(x,y)]
        
        for x in range(player.rect.topleft[0] - 64, player.rect.topleft[0] + 64):
            for y in range(player.rect.topleft[1] - 36, player.rect.topleft[1] + 36):
                if (x,y) not in self.all_objects:
                    continue
                self.active_elements[(x,y)] = self.all_objects[(x,y)]
                get_expected(x,y)
                break
                           
        
    def ysort(self, player, net_toggle):
        
        # Center player
        self.center_target(player)
        
        # Get currently active elements
        self.get_active_elements(player)
        
        
        # Instantiate active elements
        for elem_key in self.active_elements:
            sprite = self.map_dict[self.all_objects[elem_key]](elem_key, self)
            if isinstance(sprite, self.Water):
                self.change_layer(sprite, 1)
        
        for sprite in sorted([x for x in self.sprites() if self.camera_rect.colliderect(x.rect)], key=lambda sprite: sprite.layer):

            if isinstance(sprite, self.Player):
                self.change_layer(player, 2)
            
            if not net_toggle:
                if isinstance(sprite, self.Water):
                    continue
            
                
            if self.zoom_level != 1.0:
                scaled_size = (sprite.surf.get_size()[0] * self.zoom_level,
                            sprite.surf.get_size()[1] * self.zoom_level)
                    
                scaled_surf = pygame.transform.scale(sprite.surf, scaled_size)
                scaled_rect = (sprite.rect.topleft[0] * self.zoom_level, sprite.rect.topleft[1] * self.zoom_level)
                offset_pos = sprite.rect.topleft - self.offset
                offset_pos = scaled_rect - self.offset
                self.display_surf.blit(scaled_surf, offset_pos)
            else:
                
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surf.blit(sprite.surf, offset_pos)
    
        self.display_surf.blit(player.surf, player.rect.topleft - self.offset)
        
        for sprite in sorted([x for x in self.sprites() if not self.camera_rect.colliderect(x.rect)], key=lambda sprite: sprite.layer):
            self.remove(sprite)

            