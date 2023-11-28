import pygame
from sys import exit

pygame.init()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
		self.rect = self.surf.get_rect(midbottom=(50, 300))
		self.hero_index = 0

	def animate_player(self):

		global hero_index

		self.hero_index += 0.1

		if self.hero_index >= len(hero_walk):
			self.hero_index = 0
		self.surf = hero_walk[int(self.hero_index)]


class Snail(pygame.sprite.Sprite):
	def __init__(self, y_pos):
		super().__init__()
		self.surf = pygame.image.load('graphics/snail/snail1.png')
		self.surf1 = pygame.image.load('graphics/snail/snail2.png')
		self.snail_move = [self.surf, self.surf1]

		self.rect = self.surf.get_rect(midbottom=(600, y_pos))
		self.snail_index = 0

	def animate_snail(self):
		self.snail_index += 0.1
		if self.snail_index >= len(self.snail_move):
			self.snail_index = 0
		self.surf = self.snail_move[int(self.snail_index)]

	def move_snail(self, condition):
		if condition:
			self.rect.left -= 2
			if snail.rect.left <= 0:
				snail.rect.left = 600


screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('bootleg')
clock = pygame.time.Clock()

pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

hero_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
hero_surface1 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
hero_walk = [hero_surface, hero_surface1]

#snail_move_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_move_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
#snail_move = [snail_move_1, snail_move_2]
#snail_index = 0


sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
sky_rect = sky_surface.get_rect(topleft=(0,0))

ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = pixel_font.render('Furiously Fast Snails 2', True, 'Black')
text_rect = text_surface.get_rect(center=(350, 50))

#snail1 = Snail(340)
#snail2 = Snail(370)

hero_index = 0

player = Player()
#hero_rect = hero_surface.get_rect(center= (50, 300))

#snail_x_pos = 600
#snail1_x_pos = 600
running = True
held_keys = []

snail = Snail(340)

def check_held(held_keys):
	global player
	speed = 4
	for x in held_keys:
		if len(held_keys) > 1:
			speed = 2
		if 'up' in held_keys:
			player.rect.top -= speed
		if 'left' in held_keys:
			player.rect.left -= speed
		if 'right' in held_keys:
			player.rect.right += speed
		if 'down' in held_keys:
			player.rect.bottom += speed

while running:
	condition = True
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if player.rect.collidepoint(event.pos):
				print('clicked player')
			elif snail.rect.collidepoint(event.pos):
				print('clicked snail')
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				held_keys.append('up')
			elif event.key == pygame.K_s:
				held_keys.append('down')
			elif event.key == pygame.K_a:
				held_keys.append('left')
			elif event.key == pygame.K_d:
				held_keys.append('right')
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				held_keys.remove('up')
			elif event.key == pygame.K_s:
				held_keys.remove('down')
			elif event.key == pygame.K_a:
				held_keys.remove('left')
			elif event.key == pygame.K_d:
				held_keys.remove('right')

	check_held(held_keys)
	if len(held_keys) > 0:
		player.animate_player()
	else:
		player.surf = hero_walk[0]

	#snail_x_pos -= 1
	#snail1_x_pos -= 2
	screen.blit(ground_surface,(0,300))
	screen.blit(sky_surface, sky_rect)
	screen.blit(snail.surf, snail.rect)
	snail.animate_snail()

	if player.rect.colliderect(snail.rect):
		condition = False
	else:
		condition = True

	snail.move_snail(condition)


	pygame.draw.rect(screen, 'pink', text_rect)
	screen.blit(text_surface, text_rect)

	screen.blit(player.surf, player.rect)


	pygame.display.update()
	clock.tick(60)

