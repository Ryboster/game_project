import pygame, sys
import csv

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,group):
        super().__init__(group)
        self.surf = pygame.image.load('player.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.max_speed = 10
        self.acceleration = 0.1
        
    def input(self):
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        
        if up:
            self.direction.y = -1
        elif down:
            self.direction.y = 1
        elif not up and not down and self.speed > 0.1 and (left or right):
            self.direction.y = 0  
                        
        if right:
            self.direction.x = 1
        elif left:
            self.direction.x = -1
        elif not right and not left and self.speed > 0.1 and (up or down):
            self.direction.x = 0
            
        if not up and not down and not right and not left:
            self.speed /= 1.3
            if self.speed <= 0.1:
                self.direction.x = 0
                self.direction.y = 0
            
    def update(self):
        self.input()
        
        self.speed += self.acceleration
        self.speed = min(self.speed, self.max_speed)
        
        #self.rect.center += self.direction * self.speed
        
        if self.direction.x and not self.direction.y:
            self.rect.center += self.direction * self.speed
        elif self.direction.y and not self.direction.x:
            self.rect.center += self.direction * self.speed
        elif self.direction.y and self.direction.x:
            self.rect.center += (self.direction / 1.5) * self.speed
            

class Water(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        surf = pygame.image.load('water_tile.png').convert_alpha()
        self.surf = pygame.transform.scale(surf, (50,50))
        self.rect = self.surf.get_rect(topleft=pos)
        self.surf.set_colorkey((0,0,0))
        
        
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        
        # Camera rect
        wh = self.display_surf.get_size()
        self.camera_rect = pygame.Rect(50,50, wh[0] - 100, wh[0] - 300)
        
    
    def box_camera(self,target):
        self.camera_rect.center = target.rect.center
        
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y
        
    def custom_draw(self, player):
        
        
        self.box_camera(player)
        
        for tile in sorted(self.sprites(), key=lambda tile: tile.rect.centery):
            if isinstance(tile, Water):
                if tile.rect.bottomright > self.camera_rect.bottomright:
                    pass
                elif tile.rect.left < self.camera_rect.left:
                    pass
                elif tile.rect.bottom < self.camera_rect.top:
                    pass
                elif tile.rect.top > self.camera_rect.bottom:
                    pass
                else:
                    offset_pos = tile.rect.topleft - self.offset
                    self.display_surf.blit(tile.surf, offset_pos)
            else:
                pass
        
        self.display_surf.blit(player.surf, player.rect.topleft - self.offset)
        pygame.draw.rect(self.display_surf, 'yellow', (50, 50, 700, 500), 5)
        
map_dict = {
    'w': Water
}

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect(topleft=(0,0))

clock = pygame.time.Clock()


camera_group = CameraGroup()
player = Player((screen.get_size()[0] // 2, screen.get_size()[0] // 2), camera_group)


x = 0
y = 0
iters = 0

with open('tiles.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for current_tile in row:
            tile = map_dict[current_tile]((x, y), camera_group)
            x += 50
        if iters % 2 == 0:
            x = 0
            y += 15
        else:
            x = 25
            y += 15


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    screen.fill((0,0,0))
    camera_group.update() 
    camera_group.custom_draw(player)
    pygame.display.update()
    clock.tick(60)
            