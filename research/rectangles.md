
Rectangles in pygame are objects storing location on screen. They allow for a more tailored placing of our elements with their 

# Rectangles

Rectangle is an additional layer for image surfaces. It allows for changing the origin point on the surface. <br>

Rectangles have 2 core functions:<br>
* Precise positioning of surfaces<br>
* Basic Collisions<br>

The image information is stored in the surface. The position information is stored in the rectangle. You're splitting your image into two different variables which you have to control 
together.<br>

### Defining a rectangle

To define a rectangle, we first must familiarize ourselves with rectangle points:<br>

![rectangle object](./assets/rectangle_position.png 'rectangle positions') 

These are all rectangle origin points that can be grabbed. By grabbing a rectangle point, you can then place that point at your given coordinates.<br>

There are two methods of defining a rectangle:

#### ```pygame.Rect()```

This method is the least convenient for working with image surfaces due to its need of defining size.<br>

```python
rectangle_obj = pygame.Rect(left,top,width,height)
```
There is however a way of defining a rectangle around an image surface:<br>

#### ```image_surface.get_rect()```
```python
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300)) # Midbottom point placed at 80,300
```
Then you can place image surfaces inside the rectangle by passing the rectangle object as a position parameter inside ```screen.blit()```.<br>

```python
while True:
	screen.blit(player_surface, player_rectangle)
```

## Rectangle properties

Rectangle objects have 5 properties that can be used to access and manipulate the position of the rectangle:<br>

```python
rect.left // The X coordinate of the left side of the rectangle, e.g. (100)
rect.right // The X coordinate of the right side of the rectangle, e.g. (150)
rect.center // The X and Y coordinates of the center of the rectangle, e.g. (75, 75)
rect.top // The Y coordinate of the top side of the rectangle, e.g. (0)
rect.bottom // The Y coordinate of the bottom side of the rectangle, e.g. (200)
```

Those properties store X and Y coordinate values. Those values can be accessed, printed and edited to alter the position of the rectangle on screen. Consider the following example:<br>

```python
snail_surf = pygame.image.load('snail.png')
snail_rect = snail_surf.get_rect(midbottom=(100, 100))

while running:
	snail_rect.left -= 5
	screen.blit(snail_surf, snail_rect)
	
```
In this example, we edit the position of the left side of the snail rectangle in every tick, which effectively moves the whole rectangle to the left.<br>
