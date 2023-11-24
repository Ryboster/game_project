# Collisions in pygame

## Rectangles

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

#### ```image_surface_object.get_rect()```
```python
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300)) # Midbottom point placed at 80,300
```
Then you can place image surfaces inside the rectangle by passing the rectangle object as a position parameter inside ```screen.blit()```.<br>

```python
while True:
	screen.blit(player_surface, player_rectangle)
```

This set up may be quite cumbersome due to the intrinsic need of defining 2 separate variables. Later we'll learn how to combine the two in a ```sprite``` class.<br>

###

