class CharacterStatistics:
    def __init__(self, hp, max_hp, mana, max_mana, speed, acceleration, max_speed, strength, capacity, gold, experience, level):

        self.hp = hp
        self.max_hp = max_hp
        self.mana = mana
        self.max_mana = max_mana

        self.speed = speed
        self.acceleration = acceleration
        self.max_speed = max_speed
        
        self.strength = strength
        self.attack = 5 + (strength / 2)
        self.capacity = capacity

        self.gold = gold
        self.level = level
        self.exp = experience

