import pygame

class UserInterface(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.ui = pygame.sprite.Group()
        self.screen = screen

        # Create sprites for "just life" and "life bar"
        self.just_life = pygame.sprite.Sprite()
        self.just_life.image = pygame.image.load('./images/just_life.png').convert_alpha()
        self.just_life.rect = self.just_life.image.get_rect(topleft=(115, 40))
        self.just_life.image = pygame.transform.scale(self.just_life.image, (208,30))

        self.life_bar = pygame.sprite.Sprite()
        self.life_bar.image = pygame.image.load('./images/life_bar.png').convert_alpha()
        self.life_bar.rect = self.life_bar.image.get_rect(topleft=(0, 0))

        self.map = pygame.sprite.Sprite()
        self.map.image = pygame.image.load('./images/map_bg.png').convert_alpha()
        self.map.rect = self.map.image.get_rect(topright=((screen.get_size()[0]), 0))

        self.quick_slot_bar = pygame.sprite.Sprite()
        self.quick_slot_bar.image = pygame.image.load('./images/quick_slot_bar.png').convert_alpha()
        self.quick_slot_bar.rect = self.quick_slot_bar.image.get_rect(midtop=((screen.get_size()[0] ), 650))
        self.quick_slot_bar.image = pygame.transform.scale(self.quick_slot_bar.image, (800,100))
        
        self.log_scroll = pygame.sprite.Sprite()
        self.log_scroll.image  = pygame.image.load('./images/log_scroll.png').convert_alpha()
        self.log_scroll.rect = self.log_scroll.image.get_rect(topleft=(-30, 600))

        self.menu = pygame.sprite.Sprite()
        self.menu.image = pygame.image.load('./images/menu.png').convert_alpha()
        self.menu.rect = self.menu.image.get_rect(midtop=((screen.get_size()[0] // 2+40), 0))
        # Add both sprites to the ui group
        self.ui.add(self.just_life, self.life_bar,self.menu,self.map,self.log_scroll,self.quick_slot_bar)
        #self.ui.add()
    def display_ui(self):
    
        # Blit all sprites in the ui group
        self.ui.draw(self.screen)