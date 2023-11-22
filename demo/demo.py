import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('bootleg')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_surface1 = pygame.image.load('graphics/snail/snail2.png')

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = pixel_font.render('Furiously Fast Snails 2', True, 'Black')

snail_x_pos = 600
snail1_x_pos = 600
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	snail_x_pos -= 1
	snail1_x_pos -= 2
	screen.blit(ground_surface,(0,300))
	screen.blit(sky_surface,(0,0))
	screen.blit(text_surface,(200, 100))
	
	screen.blit(snail_surface,(snail_x_pos, 300))
	screen.blit(snail_surface1,(snail1_x_pos, 340))
	
	if snail_x_pos <= 0:
		snail_x_pos = 600
	if snail1_x_pos <= 0:
		snail1_x_pos = 600
	
	pygame.display.update()
	clock.tick(60)

