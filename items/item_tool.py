import os
import json


# item_name = input('Item name')

class ItemCreator:
    def __init__(self):
        self.icon = str
        self.name = str
        self.weight = float
        self.consumable = bool
        self.equippable = bool
        self.value = int
        self.durability = float
        self.stackable = bool
        self.description = str
        self.min_lvl = int
        self.required_skills = []

    def prompt_name(self):
        self.name = input('Enter item name: ')
        self.confirm = input(f'{self.name} \n Confirm? y/n	')
        if self.confirm != 'y' or self.confirm == 'n':
            self.prompt_name()
        self.confirm = 'n'

    def prompt_weight(self):
        self.weight = input('Enter item weight: ')
        try:
            self.weight = float(self.weight)
            self.confirm = input(f'{self.weight} \n Confirm? y/n	')
            if self.confirm != 'y' or self.confirm == 'n':
                self.prompt_weight()

        except ValueError:
            self.prompt_weight()
        self.confirm = 'n'

    def prompt_value(self):
        self.value = input('Enter base value: ')
        try:
            self.value = int(self.value)
            self.confirm = None
            self.confirm = input(f'\n{self.value}\nConfirm? y/n	')
            if self.confirm != 'y' or self.confirm == 'n':
                print(self.confirm)
                self.prompt_value()

        except ValueError:
            self.prompt_value()
        self.confirm = 'n'

    def prompt_durability(self):
        self.durability = input('Enter max durability (default is 1.0): ')
        try:
            self.durability = float(self.durability)
            self.confirm = input(f'\n{self.durability}\nConfirm? y/n	')
            if self.confirm == 'n' or self.confirm != 'y':
                self.prompt_durability()

        except ValueError:
            self.prompt_durability()

    def prompt_description(self):
        self.description = input('Enter item description: ')
        confirm = input(f'{self.description}\n Confirm? y/n	')
        if confirm != 'y' or confirm == 'n':
            self.prompt_description()

    def prompt_min_lvl(self):
        self.min_lvl = input('Enter minimum level to use the item: ')
        try:
            self.min_lvl = int(self.min_lvl)
            self.confirm = input(f'\n{self.min_lvl}\nConfirm? y/n	')
            if self.confirm == 'y':
                return
            else:
                self.prompt_min_lvl()

        except ValueError:
            self.prompt_min_lvl()
        self.confirm = 'n'

    def prompt_req_skills(self):

        running = True
        self.confirm = None

        while running:

            print(self.required_skills)
            req_skill = input('List required skills.\n\'y\' to confirm\n\'n\' to repeat\n> ')

            if req_skill == 'y':
                status = False
                print(f'running changed {running}')
                break
            elif req_skill == 'n':
                self.required_skills.clear()
                continue

            elif req_skill != 'n' and req_skill != 'y':
                self.confirm = input(f'{req_skill} \nConfirm? y/n	')

                if self.confirm == 'n' and self.confirm != 'y':
                    continue

                elif self.confirm == 'y':
                    self.required_skills.append(req_skill)
                    print(self.required_skills)
                    continue

        self.confirm = 'n'
        return

    def create_file(self):
        filename = input('Enter filename: ')
        confirm = input(f'save changes to {filename}.json? y/n	')
        if confirm == 'y':
            filepath = os.path.join(filename + '.json')
            with open(filepath, 'w') as new_file:
                json.dump(self.final_dict, new_file)

        elif confirm == 'n' or confirm != 'y':
            self.create_file()

    def prompt_damage_modifier(self):

        while True:
            self.dmd = input('Enter damage modifier (float)	> ')

            try:
                self.dmd = float(self.dmd)
                confirm = input(f'{self.dmd} \n Confirm? y/n	')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break

            except ValueError:
                continue

        self.confirm = 'n'

    def prompt_damage(self):
        while True:
            min_dmg = input('enter minimum damage 	> ')
            try:
                min_dmg = int(min_dmg)
                break
            except ValueError:
                continue

        while True:
            max_dmg = input('enter maximum damage 	> ')
            try:
                max_dmg = int(max_dmg)
                break
            except ValueError:
                continue

        self.damage = (min_dmg, max_dmg)

    def prompt_attack_speed(self):
        while True:
            a_s = input('Enter attack speed 	> ')
            try:
                a_s = float(a_s)
                break
            except ValueError:
                continue

        self.attack_speed = a_s

    def prompt_range(self):
        while True:
            range = input('Enter range 	> ')
            try:
                range = float(range)
                break
            except ValueError:
                continue

        self.range = range

    def prompt_defense(self):
        while True:
            defense = input('Enter defense 	> ')
            try:
                defense = int(defense)
                break
            except ValueError:
                continue

        self.defense = defense

    def prompt_hands(self):
        while True:
            hands = input('How many hands to hold the item? 1/2	> ')
            try:
                hands = int(hands)
                if hands != 1 and hands != 2:
                    continue
                else:
                    break
            except ValueError:
                continue

        self.hands = hands

    def prompt_crit_chance(self):
        while True:
            crit_chance = input('Enter crit chance (float) 		> ')
            try:
                crit_chance = float(crit_chance)
                break
            except ValueError:
                continue
        self.crit_chance = crit_chance

    def prompt_speed_modifier(self):
        while True:
            speed_mod = input('Enter speed modifier 	> ')
            try:
                speed_mod = float(speed_mod)
                break
            except ValueError:
                continue

        self.speed_modifier = speed_mod

    def prompt_weapon_type(self):
        types = {1: 'melee', 2: 'ranged', 3: 'magic'}
        while True:
            self.type = input('Select one of the following weapon types:\n1: melee		2: ranged	3: magic')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3:
                    continue
                else:
                    self.type = types[int(self.type)]
                    break
            except ValueError:
                continue

    def prompt_armor_type(self):
        types = {1: 'helmet', 2: 'chest', 3: 'legs', 4: 'boots', 5: 'shield'}
        while True:
            self.type = input(
                'Select one of the following armor types:\n1: helmet		2: chest	3: legs\n4: boots 	5: shield')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3 and int(self.type) != 4 and int(
                        self.type) != 5:
                    continue
                else:
                    self.type = types[int(self.type)]
                    break
            except ValueError:
                continue

    def prompt_tool_type(self):
        types = {1: 'pickaxe', 2: 'shovel', 3: 'hoe', 4: 'rope', 5: 'watering can', 6: 'scythe', 7: 'fishing rod',
                 8: 'trap'}
        while True:
            self.type = input(
                'Select one of the following tool types:\n1: pickaxe		2: shovel 		3: hoe\n4: rope		5: watering can		6: scythe\n7: fishing rod		8: trap')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3 and int(self.type) != 4 and int(
                        self.type) != 5 and int(self.type) != 6 and int(self.type) != 7 and int(self.type) != 8:
                    continue
                else:
                    self.type = types[int(self.type)]
                    break
            except ValueError:
                continue

    def prompt_category(self):
        while True:
            classes = {1: 'weapon', 2: 'armor', 3: 'accessory', 4: 'tool', 5: 'consumable', 6: 'quest item'}
            self.category = input(
                'select one of the following item classes:\n1: weapon	2: armor	3: accessory\n4: tool	5: consumable	6: quest item\n\n')
            try:
                self.category = int(self.category)
            except ValueError:
                continue

            if int(self.category) not in list(classes.keys()):
                print(f'\n{self.category} not in {list(classes.keys())}\n')
                continue
            if int(self.category) in list(classes.keys()):
                self.category = classes[self.category]
                break


    def prompt_duration(self):
        while True:
            self.duration = input('Enter duration in seconds    > ')
            try:
                self.duration = int(self.quantity)
                break
            except ValueError:
                continue


    def prompt_quantity(self):
        while True:
            self.quantity = input('Enter maximum number of item in stack    > ')
            try:
                self.quantity = int(self.quantity)
                break
            except ValueError:
                continue


item = ItemCreator()
item.prompt_name()
item.prompt_weight()
item.prompt_value()
item.prompt_description()

item.prompt_category()
print(item.category)

if item.category == 'weapon':
    item.prompt_weapon_type()
    item.prompt_damage_modifier()
    item.prompt_damage()
    item.prompt_attack_speed()
    item.prompt_range()
    item.prompt_hands()
    item.prompt_crit_chance()
    item.prompt_min_lvl()
    item.prompt_req_skills()
    item.final_dict = {
        'name': item.name,
        'equippable': True,
        'type': item.type,
        'damage_modifier': item.dmd,
        'damage': item.damage,
        'attack_speed': item.attack_speed,
        'range': item.range,
        'hands': item.hands,
        'crit_chance': item.crit_chance,
        'required_lvl': item.min_lvl,
        'description': item.description
    }


elif item.category == 'armor':
    item.prompt_armor_type()
    item.prompt_speed_modifier()
    item.prompt_defense()
    item.prompt_min_lvl()

    item.final_dict = {
        'name': item.name,
        'type': item.type,
        'equippable': True,
        'speed_modifier': item.speed_modifier,
        'defense': item.defense,
        'required_lvl': item.min_lvl,
        'weight': item.weight,
        'value': item.value,
        'description': item.description,
        'id': 'placeholden'
    }

elif item.category == 'consumable':
    item.prompt_duration()
    item.prompt_quantity()

    item.final_dict = {
        'name': item.name,
        'weight': item.weight,
        'description': item.description,
        'value': item.value,

        'duration': item.duration,
        'quantity': item.quantity,

        'id': 'placeholder'
    }

elif item.category == 'tool':

    item.prompt_min_lvl()
    item.prompt_durability()

    item.final_dict = {
        'name': item.name,
        'equippable': True,
        'required_lvl': item.min_lvl,
        'durability': item.durability,
        'weight': item.weight,
        'value': item.value,
        'description': item.description,
        'id': 'placeholder'
    }

elif item.category == 'accessory':
    item.prompt_damage_modifier()
    item.prompt_attack_speed()
    item.prompt_speed_modifier()
    item.prompt_defense()

    item.final_dict = {
        'name': item.name,
        'weight': item.weight,
        'value': item.value,
        'equippable': True,
        'damage_modifier': item.dmd,
        'attack_speed': item.attack_speed,
        'speed_modifier': item.speed_modifier,
        'defense': item.defense,
        'description': item.description,
        'id': 'placeholder'

    }
elif item.category == 'quest item':
    item.final_dict = {
        'name': item.name,
        'description': item.description,
        'id': 'placeholder'

    }

item.create_file()
print('finished')
