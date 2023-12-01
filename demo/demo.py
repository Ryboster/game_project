from tabnanny import check
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

class Event_handler:
	def __init__(self, held_keys, player):
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
		self.check_held(held_keys, player)

	def check_held(self, held_keys, player):
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




screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('bootleg')
clock = pygame.time.Clock()

pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

hero_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
hero_surface1 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
hero_walk = [hero_surface, hero_surface1]


sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
sky_rect = sky_surface.get_rect(topleft=(0,-50))

ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft=(0, 250))

text_surface = pixel_font.render('Furiously Fast Snails 2', True, 'Black')
text_rect = text_surface.get_rect(center=(350, 50))

class Score:
	def __init__(self, rect_pos):

		self.x, self.y = rect_pos
		self.score = 0


	def update_score(self, second):

		self.score_surf = pixel_font.render(f'SCORE: {self.score}', True, 'Black')
		self.text_rect = self.score_surf.get_rect(center = (self.x,self.y+30))

		second += 1

		if second == 60:
			self.score += 1
			second = 0

		return second


hero_index = 0

player = Player()

running = True
held_keys = []

snail = Snail(340)
second = 0

score = Score(text_rect.center)
second = score.update_score(second)

while running:
	condition = True
	event = Event_handler(held_keys, player)


	if len(held_keys) > 0:
		player.animate_player()
	else:
		player.surf = hero_walk[0]

#	second = score.update_score(second)

	
	screen.blit(sky_surface, sky_rect)
	screen.blit(ground_surface,ground_rect)
	screen.blit(snail.surf, snail.rect)
	snail.animate_snail()

	if player.rect.colliderect(snail.rect):
		condition = False
		second = score.update_score(second)

	else:
		condition = True

	snail.move_snail(condition)

	

	pygame.draw.rect(screen, 'pink', text_rect)
	screen.blit(text_surface, text_rect)
	screen.blit(score.score_surf, score.text_rect)

	screen.blit(player.surf, player.rect)


	pygame.display.update()
	clock.tick(60)

