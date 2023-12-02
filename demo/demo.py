import pygame, sys
from random import randint


class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
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
            print(self.speed)
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
                
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        
        # Ground
        self.ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))
        
    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_W
        self.offset.y = target.rect.centery - self.half_y
    
    def custom_draw(self, player):
        
        self.center_target(player)
        
        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surf.blit(self.ground_surf,ground_offset)
        
        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.image, offset_pos)
        
        
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

camera_group = CameraGroup()
player = Player((640, 360), camera_group)
trees = []


''' 
        if up:
            self.direction.y = -1
        elif down:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if right:
            self.direction.x = 1
        elif left:
            self.direction.x = -1
        else:
            self.direction.x = 0
        '''    
for i in range(20):
    random_x = randint(0, 1000)
    random_y = randint(0, 1000)
    x = Tree((random_x, random_y), camera_group)
    trees.append(x)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    screen.fill('#71ddee')
        
    camera_group.update()
    camera_group.custom_draw(player)
        
    pygame.display.update()
        
    clock.tick(60)