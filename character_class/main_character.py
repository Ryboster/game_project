import pygame
from states import states_table as states
from effects import effects_table as effects
import time
from stats_class import CharacterStatistics as char_stats

class Character:
    def __init__(self):
        self.stats = char_stats(hp = 100,
                                max_hp = 100,
                                mana = 100,
                                max_mana = 100,
                                speed = 2,
                                strength = 5,
                                capacity = 100,
                                gold = 1000,
                                experience = 0,
                                level = 1)

    def state(self, state):
        self.state = state

    def use(self, item):
        print(item)

    def apply_effect(self, effect):
        self.state(effect)

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

    def attack(self, target):
        target.take_damage(self.stats.attack)


jeff = Character()
jeff.display_info()
