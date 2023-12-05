import pygame, sys
import csv
import numpy as np

pygame.init()

file = open('map.csv', 'r')
csv_file = csv.reader(file)

#with open('map.csv', 'r') as file:
#    csv_file = csv.reader(file)

csv2_file = csv.reader(file)

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
        

class Water(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = pygame.image.load('water_tile.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (64,64))
        self.rect = self.surf.get_rect(topleft=pos)
        self.surf.set_colorkey((0,0,0))


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
        self.myArray = [['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w']]
        k = np.array(self.myArray)

        
    def chunk_world(self, world, player):
        self.world = world   
        player_pos = (int(world[0] // 64), int(world[1] // 64))

        visible_tiles = []

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
            if isinstance(sprite, type(player)):
                pass

            player_pos = self.get_xy(player)
            
            player_offset = sprite.rect.topleft - self.offset
            #player_pos = player.rect.center
            sprite_pos = self.get_xy(sprite)

            #print(sprite_pos)
            #print(player_pos)

            #if sprite_pos == player_pos:
            #    screen.blit(sprite.surf, player_offset)
                #print((sprite.rect.x // 64))

                #print(self.myArray[(sprite.rect.x // 64) - 1: (sprite.rect.x // 64) + 2 ])

        #    [x-1: x+2,  y-1: y+2]
        #    if sprite.rect.x 

            player_offset = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.surf, player_offset)

        player_offset = player.rect.topleft - self.offset
        self.display_surf.blit(player.surf, player_offset)
        #print(player.rect.x // 64, player.rect.y //64)

    
    def get_xy(self, target):

        return (target.rect.x // 64,
                target.rect.y //64)
    
    def create_map(self, k,Water,player):
        results = self.get_xy(player)
        print(results[0],results[1])
        
        x= results[0]
        if (x <= 0):
            x=1

        y = results[1]
        #print(y)
        if(y<=0):
            y=1
        #[int(y-1): int((x+2)), int(y-1): (y+2)]    
        #print(k[1:4, 1:4])
        print( k ) # (y-1): (y+2)] ) 
        #print(k[(x-1): (x+2), (y-1): (y+2)])
        #print(k,k[x-1: x+2])
        new_k= k[int(y-1): int((x+2)), int(y-1): (y+2)]
        x = 0
        y = 0
        for row in new_k:
            for col in row:
                if col == 'w':
                    #Water((x,y), camera_group)
                    self.add(Water((x,y)))
                x += 64
            x = 0
            y += 64
      


camera_group = CameraGroup()
player = Player((0,0), camera_group)

myArray = [['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w'],['w','w','w','w','w']]
k = np.array(myArray)
#print(camera_group.get_xy(player,k))




while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.image.save(screen,'map.png')
                pygame.quit()
                sys.exit()
                
    camera_group.create_map(k,Water,player)
    camera_group.chunk_world(world, player)
    camera_group.custom_draw(player)
    
    camera_group.update()
    
    pygame.display.update()