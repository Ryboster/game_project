import pygame
from states import states_table as states
from effects import effects_table as effects
import time
from stats_class import CharacterStatistics as char_stats

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init()
        self.stats = char_stats(hp = 100,
                                max_hp = 100,
                                mana = 100,
                                max_mana = 100,
                                speed = 2,
                                acceleration = 0.1,
                                max_speed = 10,
                                strength = 5,
                                capacity = 100,
                                gold = 1000,
                                experience = 0,
                                level = 1)
        self.inventory = []
        self.equipment = {
            'head': None,
            'chest': None,
            'legs': None,
            'feet': None,
            'ring1': None,
            'ring2': None,
            'necklace': None,
            'left_hand': None,
            'right_hand': None}
        
        self.direction = pygame.math.Vector2()
        self.speed = self.stats.speed
        self.max_speed = self.stats.max_speed
        self.acceleration = self.stats.acceleration

    def equip_item(self, item, slot):
        if item in self.inventory and self.equipment[slot] == None:
            self.inventory.remove(item)
            self.equipment[slot] == item
        elif item in self.inventory and self.equipment[slot] != None:
            self.inventory.remove(item)
            self.inventory.append(self.equipment[slot])
            self.equipment[slot] = item

    def change_state(self, state):
        self.state = state

    def take_damage(self, damage):
        self.stats.hp -= damage
        if self.stats.hp <= 0:
            print('you were strangled by a fish and died')

    def heal(self, amount):
        self.stats.hp += amount
        if self.stats.hp >= 100:
            self.stats.hp = 100
            print('fully healed')

    def gain_experience(self, experience):
        self.stats.exp += experience

    def level_up(self):
        self.stats.level += 1

    def display_info(self):
        print(f'''
        HP: {self.stats.hp}/{self.stats.max_hp}\n
        Mana: {self.stats.mana}/{self.stats.max_mana}\n
        ${self.stats.gold}\n''')

    def attack(self, target, damage):
        target.take_damage(damage)


    def input(self):
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        
        if up:
            self.direction.y = -1
        elif down:
            self.direction.y = 1
        elif not up and not down and self.speed > 0.1 and (left or right):
            self.direction.y = 0  
                        
        if right:
            self.direction.x = 1
        elif left:
            self.direction.x = -1
        elif not right and not left and self.speed > 0.1 and (up or down):
            self.direction.x = 0
            
        if not up and not down and not right and not left:
            self.speed /= 1.3
            if self.speed <= 0.1:
                self.direction.x = 0
                self.direction.y = 0
            
    def update(self):
        self.input()
        
        self.speed += self.acceleration
        self.speed = min(self.speed, self.max_speed)
        
        if self.direction.x and not self.direction.y:
            self.rect.center += self.direction * self.speed
        elif self.direction.y and not self.direction.x:
            self.rect.center += self.direction * self.speed
        elif self.direction.y and self.direction.x:
            self.rect.center += (self.direction / 1.5) * self.speed
