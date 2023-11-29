# Collisions in pygame


### ```rect1.colliderect(rect2)```
This method can be called from any defined rectangle object. It can be used to detect collision between two rectangles.<br>

```python
snail_surf = pygame.image.load('snail.png')
snail_rect = snail_surf.get_rect()

player_surf = pygame.image.load('player.png')
player_rect = player_surf.get_rect()

while running:
	screen.blit(snail_surf, snail_rect)
	screen.blit(player_surf, player_rect)
	
	if player_rect.colliderect(snail_rect):
		print('collision between player and snail')

```
<br>
In this example we define two separate rectangles and call ```colliderect``` on the player's rectangle. If player's rectangle collides with the snail's, 'collision between player and snail' will be printed.<br>

```colliderect``` returns 0 or 1 depending on whether there is collision or not. It is thanks to that that we can write collision logic.<br>


### ```rect1.collidepoint((x,y))```

This method works similarly to ```colliderect```, except that it takes coordinates instead of a rectangle object as its argument.<br>

```python
player_surf = pygame.image.load('player.png').convert_alpha()
player_rect = player_surf.get_rect()

while running:
	screen.blit(player_surf, player_rect)
	
	if player_rect.collidepoint(pygame.mouse.get_pos()):
		print('mouse on player')
```
In this example we first define a player rectangle and then check for collisions between the rectangle and the mouse. If collision is detected, 'mouse on player' is printed.<br>

