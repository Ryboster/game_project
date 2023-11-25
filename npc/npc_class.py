
class NPC:
    def __init__(self, name, hp, max_hp, mana, max_mana, gold, strength, speed):

        self.name = name

        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.max_mana = max_mana

        self.gold = gold

        self.strength = strength
        self.attack = 5 + (strength / 2)

        self.speed = speed

        self.inventory = []

    def shop(self):
        '''display shopping window'''
        pass

    def talk(self, dialogue):
        '''display dialogue'''
        pass

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def initiate_combat(self):
        '''attack player'''
        pass

    def give_quest(self, quest):
        pass

    def complete_quest(self, quest):
        pass