import pygame, sys
import csv

with open('map.csv', 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)

pygame.init()

screen = pygame.display.set_mode((1280, 720))
width, height = screen.get_size()

world = pygame.math.Vector2((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,group):
        super().__init__(group)
        self.surf = pygame.image.load('player.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 1
        self.max_speed = 1
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
        self.half_w = self.display_surf.get_size()[0] // 2
        self.half_y = self.display_surf.get_size()[1] // 2
        self.wh = self.display_surf.get_size()
        

        # Camera rect
        self.camera_rect = pygame.Rect(self.offset.x, self.offset.y, self.half_w, self.half_y)
        
        ### Zoom
        self.zoom_level = 1.0 
        
    def chunk_world(self, world, player):
        self.world = world
        
        player_pos = (int(world[0] // 64), int(world[1] // 64))
        
        
        visible_tiles = []
        
        
        #print(self.world.x // 64, self.world.y // 64)
         
        #if self.world.x < 0:
        #    player_pos[0] = 0
        #else:
        #    player_pos[0] = self.world[0]
        #    #self.world.x = player.rect.center[0]
        
       # if self.world.y < 0:
        #    player_pos[1] = 0
        #else:
        #    self.world.y = player.rect.center[1]
        
        
        
        
    def box_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

        self.camera_rect.centerx = target.rect.centerx - self.offset.x
        self.camera_rect.centery = target.rect.centery - self.offset.y
        self.camera_rect.center = target.rect.center
        
    def custom_draw(self, player):
        
        # Box camera
        self.box_camera(player)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            player_offset = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.surf, player_offset)


camera_group = CameraGroup()
player = Player((0,0), camera_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.image.save(screen,'map.png')
                pygame.quit()
                sys.exit()
                
    camera_group.custom_draw(player)
    camera_group.chunk_world(world, player)
    camera_group.update()
    #screen.fill((255,255,255))
    pygame.display.update()