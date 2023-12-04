import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf = pygame.image.load('demo/graphics/Player/player_walk_1.png').convert_alpha()
		self.rect = self.surf.get_rect(midbottom=(50, 300))
		self.hero_index = 0

	# def animate_player(self):

	# 	global hero_index
	# 	self.hero_index += 0.1

	# 	if self.hero_index >= len(hero_walk):
	# 		self.hero_index = 0
	# 	self.surf = hero_walk[int(self.hero_index)]