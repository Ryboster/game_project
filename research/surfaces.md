# Surfaces

There are two different kinds of surfaces:

# Display Surface
Display surface is the bottommost layer. This surface defines the size of the window.<br>

```python
screen = pygame.display.set_mode((800,400)) # create the window
while True:
	pygame.display.update() # sustain the window
```
Initializing that surface, you need to pass it a tuple containing dimensions.<br>


# Regular surface

Regular surfaces go on top of the display surface. There can be any number of them.<br>

### Solid colour surface

```python
screen = pygame.display.set_mode((800,400)) # create the window display
surface1 = pygame.Surface((width,height)) # create a regular surface

while True:
	screen.blit(surface,(width,height)) # block image transfer
```
position is a tuple representing the position on the display surface. ```(0,0)``` (starting position) for every layer is top-left corner. Increasing either value puts the top-left corner of any subsequent surface farther away from either top or left border.<br>

### Image surfaces

Define an image surface using ```pygame.image.load('path/to/image.png')```

```python
sky_surface = pygame.image.load('sky.png')
```

Next you can display the surface using ```screen.blit(sky_surface,(width,height))```<br>


### Text surfaces
To create a text surface, you first need to define a font object using <br>
```python
pygame.font.Font('path/to/font', size)
```

Next you can create a surface object by rendering the font using ```font_var.render()```. It takes three arguments: 
* Text
* Anti-Aliasing
* Colour

```
arial = pygame.font.Font('arial.ttf', 50)
text_surface = arial.render('Hello', False, 'White')
```
Then proceed to display the surface using ```screen.blit(surface,(width,height))```<br>

```python
test_font = pygame.font.Font(Type, Size)
text_surface = test_font.render('text', Anti-Aliasing, 'colour')

screen = pygame.display.set_mode((400, 400))

while True:
	screen.blit(text_surface, (200,200))
```

### Rectangles

2 core functions:
* Precise positioning of surfaces
* Basic Collisions

Rctangles allow for changing the origin point on the surface. <br>

It is a common practice in pygame to use rectangles. The image information is stored in the surface. The position information is stored in the rectangle. You're splitting your image into two different variables which you have to control together.<br>

![rectangle object](./assets/rectangle_position.png 'rectangle positions') 

```python

```


