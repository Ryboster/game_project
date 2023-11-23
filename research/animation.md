# Animation in pygame

### Updating position

```python
snail = python.image.load('graphics/snail.png')

screen = python.display.set_mode((900,900))
snail_x_pos = 0

while True:
	
	snail_x_pos += 1
	screen.blit(snail, (snail_x_pos, 700)
	screen.update()
		
```
`
### Converting Image Surfaces

Working with textures long term you don't want to keep using .png files. You want to convert them into something that's easier to work with for pygame<br>

```python
image_surface = pygame.image.load('graphics/snail.png').convert()

```

All this does is converts the image into something pygame works on easily. Crucial optimisation step.<br>

This will not account for transparent images however. To account for that, you need to parse the alpha channel in your text format. You can do that easily by using ```convert_alpha()``` instead.<br>

```python
image_surface = pygame.image.load('graphics/snail.png').convert_alpha()
```

