# Getting started with pygame

## Installing pygame
Pygame can be installed with ```pip```. To install, use the following command:<br>
```python
pip install pygame
```

## Importing pygame
To import pygame into your script, you can use the following line:<br>
```python
import pygame
```

## Initializing pygame
create an instance of ```pygame``` class with<br>
```python
pygame.init()
```

## Creating a window
Once you've created an instance of ```pygame``` class, you can define a window by accessing pygame's ```display``` property and passing your desired resolution.<br>

```python
screen = pygame.display.set_mode([500, 500])
```
<br>

This sets up and initializes a basic game window. The window will only flash however because there is no **game loop** yet.<br>
## Creating a game loop<br>
A game loop is a simple ```while True``` loop. To create it, you need to define a boolean variable and initialize it with ```True``` and then set up a logic for it to become ```False```.<br>
```python
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
```
In this example we set up a ```while True``` loop and in it, we iterate over the **event queue**. If ```pygame.QUIT``` event is queued (i.e. if the player clicked the X), the loop is broken and the game quits.<br>

## Drawing and Filling
#### Drawing
Pygame has a ```draw``` property. This property can be used to draw rudamentary shapes on display.
Here is an example of drawing a circle in the middle of the screen:
```python
screen = pygame.display.set_mode([1280, 720])

# Calculate the middle of the screen
middle_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
	pygame.draw.circle(screen, "red", middle_position, 40)
	
```
In this example, we calculate where the middle of the screen is by accessing the width and height of the screen and halving those dimensions. We then create a ```Vector2``` object (class representing a 2D vector) and pass that object to our circle.<br>
The circle is drawn with the ```circle``` property of ```pygame.draw```, and it takes in four arguments:<br>
* ```screen``` - What display object it's being drawn on.<br>
* ```"red"``` - What colour it's filled with.<br>
* ```middle_position``` - Vector object representing its position.<br>
* ```40``` - Its size in pixels.<br>

#### Filling
A display object can be filled with solid colour:
```python
screen = pygame.display.set_mode()
screen.fill('purple')
```

