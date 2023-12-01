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
        while True:
            self.name = input('Enter item name: ')
            confirm = input(f'confirm the name of {self.name}? y/n    > ')
            if confirm != 'y' or confirm == 'n':
                continue
            elif confirm == 'y':
                break

    def prompt_weight(self):
        while True:
            self.weight = input('Enter item weight: ')
            try:
                self.weight = float(self.weight)
                confirm = input(f'confirm the weight of {self.weight}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

    def prompt_value(self):
        while True:
            self.value = input('Enter base value: ')
            try:
                self.value = int(self.value)
                confirm = input(f'confirm the value of {self.value}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break

            except ValueError:
                continue
            
            
    def prompt_durability(self):
        while True:
            self.durability = input('Enter max durability (default is 1.0)    > ')
            try:
                self.durability = float(self.durability)
                confirm = input(f'confirm the durability of {self.durability}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break

            except ValueError:
                continue

    def prompt_description(self):
        while True:
            self.description = input('Enter item description: ')
            confirm = input(f'confirm the following description?\n\n{self.description}\n y/n    > ')
            if confirm != 'y' or confirm == 'n':
                continue
            elif confirm == 'y':
                break

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
        while True:
            filename = input('Enter filename: ')
            specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', ':', ';', '[', ']', '\'', '\\', ',', '<', '>', '.', '/', '?',
                        '   ', '`', '~', '-', '=', '+']
            illegal_chars = []
            for char in filename:
                if char in specials:
                    print(f'illegal special character: {char}')
                    illegal_chars += char
            if illegal_chars:
                print('resetting ...')
                continue
            else:
                confirm = input(f'save changes to {filename}.json? y/n    > ')
                if confirm == 'y':
                    filepath = os.path.join(filename + '.json')
                    with open(filepath, 'w') as new_file:
                        json.dump(self.final_dict, new_file)
                elif confirm == 'n' or confirm != 'y':
                    continue

    def prompt_damage_modifier(self):

        while True:
            self.dmd = input('Enter damage modifier (float)	> ')

            try:
                self.dmd = float(self.dmd)
                confirm = input(f'confirm the damage modifier of {self.dmd}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break

            except ValueError:
                continue

        self.confirm = 'n'

    def prompt_damage(self):
        while True:
            min_dmg = input('enter minimum damage    > ')
            try:
                min_dmg = int(min_dmg)
                confirm = input(f'confirm min damage of {min_dmg}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        while True:
            max_dmg = input('enter maximum damage    > ')
            try:
                max_dmg = int(max_dmg)
                confirm = input(f'confirm max damage of {max_dmg}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        self.damage = (min_dmg, max_dmg)

    def prompt_attack_speed(self):
        while True:
            a_s = input('Enter attack speed    > ')
            try:
                a_s = float(a_s)
                confirm = input(f'confirm the attack speed of {a_s}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        self.attack_speed = a_s

    def prompt_range(self):
        while True:
            range = input('Enter range    > ')
            try:
                range = float(range)
                confirm = input(f'confirm the range of {range}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        self.range = range

    def prompt_defense(self):
        while True:
            defense = input('Enter defense    > ')
            try:
                defense = int(defense)
                confirm = input(f'confirm the defense of {defense}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        self.defense = defense

    def prompt_hands(self):
        while True:
            hands = input('How many hands to hold the item? (1/2)    > ')
            try:
                hands = int(hands)
                if hands != 1 and hands != 2:
                    continue
                else:
                    confirm = input(f'confirm the hands of {hands}? y/n    > ')
                    if confirm != 'y' or confirm == 'n':
                        continue
                    elif confirm == 'y':
                        break
            except ValueError:
                continue

        self.hands = hands

    def prompt_crit_chance(self):
        while True:
            crit_chance = input('Enter crit chance    > ')
            try:
                crit_chance = float(crit_chance)
                confirm = input(f'confirm the crit chance of {crit_chance}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue
        self.crit_chance = crit_chance

    def prompt_speed_modifier(self):
        while True:
            speed_mod = input('Enter speed modifier    > ')
            try:
                speed_mod = float(speed_mod)
                confirm = input(f'confirm the speed modifier of {speed_mod}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

        self.speed_modifier = speed_mod

    def prompt_weapon_type(self):
        types = {1: 'melee', 2: 'ranged', 3: 'magic'}
        while True:
            self.type = input('Select one of the following weapon types:\n1: melee    2: ranged    3: magic')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3:
                    continue
                else:
                    self.type = types[int(self.type)]
                    confirm = input(f'confirm the weapon type of {self.type}? y/n    > ')
                    if confirm != 'y' or confirm == 'n':
                        continue
                    elif confirm == 'y':
                        break
            except ValueError:
                continue

    def prompt_armor_type(self):
        types = {1: 'helmet', 2: 'chest', 3: 'legs', 4: 'boots', 5: 'shield'}
        while True:
            self.type = input(
                'Select one of the following armor types:\n1: helmet    2: chest    3: legs\n4: boots    5: shield')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3 and int(self.type) != 4 and int(
                        self.type) != 5:
                    continue
                else:
                    self.type = types[int(self.type)]
                    confirm = input(f'confirm the armor type of {self.type}? y/n    > ')
                    if confirm != 'y' or confirm == 'n':
                        continue
                    elif confirm == 'y':
                        break
            except ValueError:
                continue

    def prompt_tool_type(self):
        types = {1: 'pickaxe', 2: 'shovel', 3: 'hoe', 4: 'rope', 5: 'watering can', 6: 'scythe', 7: 'fishing rod',
                 8: 'trap'}
        while True:
            self.type = input(
                'Select one of the following tool types:\n1: pickaxe    2: shovel    3: hoe\n4: rope    5: watering can    6: scythe\n7: fishing rod    8: trap')
            try:
                self.type = int(self.type)
                if int(self.type) != 1 and int(self.type) != 2 and int(self.type) != 3 and int(self.type) != 4 and int(
                        self.type) != 5 and int(self.type) != 6 and int(self.type) != 7 and int(self.type) != 8:
                    continue
                else:
                    self.type = types[int(self.type)]
                    confirm = input(f'confirm the tool type of {self.type}? y/n    > ')
                    if confirm != 'y' or confirm == 'n':
                        continue
                    elif confirm == 'y':
                        break
            except ValueError:
                continue

    def prompt_category(self):
        while True:
            classes = {1: 'weapon', 2: 'armor', 3: 'accessory', 4: 'tool', 5: 'consumable', 6: 'quest item'}
            self.category = input(
                'select one of the following item classes:\n1: weapon    2: armor    3: accessory\n4: tool    5: consumable    6: quest item\n\n')
            try:
                self.category = int(self.category)
            except ValueError:
                continue

            if int(self.category) not in list(classes.keys()):
                print(f'\n{self.category} not in {list(classes.keys())}\n')
                continue
            if int(self.category) in list(classes.keys()):
                self.category = classes[self.category]
                confirm = input(f'confirm category of {self.category}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break


    def prompt_duration(self):
        while True:
            self.duration = input('Enter duration in seconds    > ')
            try:
                self.duration = int(self.duration)
                confirm = input(f'Confirm duration of {self.duration}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue


    def prompt_quantity(self):
        while True:
            self.quantity = input('Enter maximum number of item in stack    > ')
            try:
                self.quantity = int(self.quantity)
                confirm = input(f'Confirm quantity of {self.quantity}? y/n    > ')
                if confirm != 'y' or confirm == 'n':
                    continue
                elif confirm == 'y':
                    break
            except ValueError:
                continue

    def calculate_id(self):
        self.highest_id = 0
        for filename in os.listdir('./'):
            if filename.endswith('.json'):
                with open(filename, 'r') as item:
                    data = json.load(item)
                id = data['id']
                try:
                    id = int(id)
                    if self.highest_id < id:
                        self.highest_id = id
                except ValueError:
                    continue
        self.highest_id += 1


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
    item.calculate_id()
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
        'description': item.description,
        'required_skills': item.required_skills,
        'id': item.highest_id
    }


elif item.category == 'armor':
    item.prompt_armor_type()
    item.prompt_speed_modifier()
    item.prompt_defense()
    item.prompt_min_lvl()
    item.calculate_id()

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
        'id': item.highest_id
    }

elif item.category == 'consumable':
    item.prompt_duration()
    item.prompt_quantity()
    item.calculate_id()

    item.final_dict = {
        'name': item.name,
        'weight': item.weight,
        'description': item.description,
        'value': item.value,

        'duration': item.duration,
        'quantity': item.quantity,

        'id': item.highest_id
    }

elif item.category == 'tool':

    item.prompt_min_lvl()
    item.prompt_durability()
    item.calculate_id()

    item.final_dict = {
        'name': item.name,
        'equippable': True,
        'required_lvl': item.min_lvl,
        'durability': item.durability,
        'weight': item.weight,
        'value': item.value,
        'description': item.description,
        'id': item.highest_id
    }

elif item.category == 'accessory':
    item.prompt_damage_modifier()
    item.prompt_attack_speed()
    item.prompt_speed_modifier()
    item.prompt_defense()
    item.calculate_id()

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
        'id': item.highest_id

    }
elif item.category == 'quest item':
    item.calculate_id()
    item.final_dict = {
        'name': item.name,
        'description': item.description,
        'id': item.highest_id

    }

item.create_file()
print('finished')
