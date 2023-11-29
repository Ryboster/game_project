# Sprite class in pygame

### Definition
Sprite class in pygame is a way of combining rectangles with surfaces in a single object. For example:<br>

```python
class Player(pygame.sprite.Sprite)
	def __init__(self):
	super().__init__()
	
	self.surf = pygame.image.load('image.png')
	self.rect = self.surf.get_rect(topleft=(0,0))

player = Player()

while running:
	screen.blit(player.surf, player.rect)
```

While this can be accomplished without inheriting from the Sprite class, doing so holds certain advantages over not using the class:<br>


### Grouping and Updating

Members of the ```Sprite``` class can be grouped together to ease the drawing and updating process for multiple sprites simultaneously.<br>

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(0, 0))

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


while True:

    all_sprites.update()  # Update all sprites in the group

    all_sprites.draw(screen) # Draws all sprites in the group
    pygame.display.flip()
```

In this example we define an instance of the ```Player``` class which inherits from the ```Sprite``` class. Then we define an instance of the ```Group``` class, and we call its ```add()``` method, passing the Player class instance as a parameter.<br>
With this, we can then refer to the group object to affect all of its members.<br>

### Collision detection

pygame defines more efficient collision detection methods for sprites; ```pygame.sprite.spritecollide```. It allows for checking collision between one sprite and a group of sprites, as well as for automatic killing of sprites when collision is detected.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(0, 0))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(200, 0))

player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy)

while True:

    all_sprites.update()  # Update all sprites in the group

    # Check for collision using sprite groups
    collisions = pygame.sprite.spritecollide(player, [enemy], False)
    if collisions:
        print("Collision!")

    all_sprites.draw(screen)
    pygame.display.flip()
```

In this example, we check for collisions between the player and a **list** of enemies. If collision is detected, the enemy sprites remain on the screen, and 'Collision!' is printed.<br>

The syntax is as follows:
```python
pygame.sprite.spritecollide(sprite, group, dokill)
```
* ```sprite``` parameter is your center sprite you want to check collisions for.<br>
* ```group``` parameter takes in an iterable object of sprites to detect collision with.<br>
* ```dokill``` parameter takes a boolean value (True/False).<br>
	* if True: It kills the sprites on collision.<br>
	* if False: Sprites remain on collision.<br>
