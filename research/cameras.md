# Cameras in pygame

### Y sort camera
Y sort camera decides which object on screen should be in front of another.<br>
It works by comparing Y position of all sprites and rendering objects in ascending order.<br>

```python
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        
    def custom_draw(self,):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surf.blit(sprite.image, sprite.rect)
```
The ```CameraGroup``` class inherits from ```pygame.sprite.Group``` class to get access to all sprites.
On call to ```CameraGroup.custom_draw()```, the script iterates through the center y position of every sprite in order from lowest to highest and blits the objects on the screen. This way things appear in the right order.


```python
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector()
        
        # Ground
        self.ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))
        
    def custom_draw(self,):
    	# Ground
    	self.display_surf.blit(self.ground_surf, self.ground_rect)
    	
    	# Active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surf.blit(sprite.image, sprite.rect)
```

### Player centered camera

A player centered camera is a moving camera which centers the player sprite in the middle of the screen and draws each element according to player's position.<br>

#### How does a moving camera work?

A moving camera works by applying camera offset to every drawn sprite's position. The farther the camera moves, the greater the offset, thus the object is drawn farther away.<br>

We define the offset as an instance of the ```Vector2``` class. <br>

The ```pygame.math.Vector2``` class represents a 2D vector and its instances have attributes ```x``` and ```y``` representing components of the vector. Those attributes' values can be accessed, changed, and used in mathematical operations.<br>

After creating the offset object, we define ```offset.x``` and ```offset.y``` as player position minus half the width and height of the game window. We then subtract that amount from every drawn object's ```x``` and ```y``` attributes on movement to move them in the opposite direction to camera movement.<br>

### camera

Player centered camera is a camera which dynamically applies the offset to every drawn object's position.<br>

To center our player sprite in the middle of the screen, we define the ```x``` and ```y``` attributes of the ```self.offset``` object as the player's position minus half of the screen's width and height. This way, the player is always in the middle of the offset.

```python
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
```

In the example above, we modify our previously defined class ```CameraGroup``` by adding the offset and the function ```center_target```. The new function updates the offset once every tick by getting the position of the player object and subtracting half the screen's width and height.<br>

With the offset object being updated, we then draw remaining sprites using that object.<br>

