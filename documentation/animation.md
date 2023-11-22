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

### Animation
