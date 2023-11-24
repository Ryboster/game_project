import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('bootleg')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface1 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = pixel_font.render('Furiously Fast Snails 2', True, 'Black')

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))

snail_rect = snail_surface.get_rect(midbottom = (600, 320))
snail_rect1 = snail_surface1.get_rect(midbottom = (600, 370))

snail_x_pos = 600
snail1_x_pos = 600
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
	
	screen.blit(ground_surface,(0,300))
	screen.blit(sky_surface,(0,0))
	screen.blit(text_surface,(200, 100))
	
	snail_rect.left -= 1
	snail_rect1.left -= 2
	screen.blit(snail_surface,snail_rect)
	screen.blit(snail_surface1,snail_rect1)

	screen.blit(player_surface,player_rectangle)
	
	
	
	if snail_rect.left <= 0:
		snail_rect.left = 600
	if snail_rect1.left <= 0:
		snail_rect1.left = 600
	
	if player_rectangle.colliderect(snail_rect):
		
	pygame.display.update()
	clock.tick(60)


