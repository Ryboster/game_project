from effects import Effects as effects
from main_character import Character as char

class Item:
    def __init__(self, icon, name, weight, consumable, equippable, effect, value, durability, stackable, description, min_lvl, required_skill):
        self.icon = icon
        self.name = name

        self.weight = weight

        self.consumable = consumable
        self.equippable = equippable

        self.effect = effect
        self.durability = durability
        self.value = value + (durability / 2)

        self.stackable = stackable

        self.required_lvl = min_lvl
        self.required_skill = required_skill

    def display_info(self):
        print(f'name: {self.name}\n',
              f'icon path:{self.icon}\n',
              f'weight: {self.weight}\n',
              f'consumable: {self.consumable}\n',
              f'equippable: {self.equippable}\n',
              f'effect: {self.effect}\n',
              f'value: ${self.value}\n',
              f'durability: {self.durability}/100\n',
              f'stackable: {self.stackable}\n',
              f'required lvl: {self.required_lvl}\n',
              f'required skill: {self.required_skill}')

    def use(self, target):
        self.effect.apply(target)

