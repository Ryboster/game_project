# Animation in pygame

### Updating position
Updating position is not animation per se, however it can be used to move surfaces on the screen which is often a prerequisite in animation.<br>

```python
snail = pygame.image.load('graphics/snail.png')

screen = python.display.set_mode((900,900))
snail_x_pos = 0

while True:
	
	snail_x_pos += 1
	screen.blit(snail, (snail_x_pos, 700)
	screen.update()
		
```
This is a very crude method of updating position. It can be vastly improved if you've defined a rectangle object for your surface:<br>

```python
snail_surf = pygame.image.load('graphics/snail.png')
snail_rect = snail_surf.get_rect(midbottom=(100,100))

while running:
	screen.blit(snail_surf, snail_rect)
	snail_rect.left -= 5
```

In this example we've defined a rectangle and we placed our surface inside it. Now to move the surface, we can simply edit the value of its ```left``` attribute.<br>

### Animation
Animation is dynamically switching between surfaces according to actions:<br>

```python
def animate_player()
	hero_surface1 = pygame.image.load('graphics/Player/player_walk_1.png').convert.alpha()
	hero_surface2 = pygame.image.load('graphics/Player/player_walk_2.png').convert.alpha()
	hero_walk_animation = [hero_surface1, hero_surface2]
	
	global hero_index
	hero_index += 0.1
	if hero_index >= len(hero_walk):
		hero_index = 0
	current_surface = hero_walk[int(hero_index)]
	return current_surface


hero_index = 0
running = True
while running:
	hero_surf = animate_player()
	screen.blit(hero_surf, (x,y))

```
In this example, we define a function that returns two different surfaces. It increments the index by 0.1 per call and then rounds the resulting value to integer so that both surfaces occur the same amount of times.<br>
This function can be put behind any logic to animate our player.<br>
