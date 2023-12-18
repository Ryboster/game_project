class Effects:
    def __init__(self, duration, effect_type, magnitude):
        print('ini')
        self.duration = duration
        self.type = effect_type
        self.magnitude = magnitude

    def apply(self, target):
        if self.type == 'heal':
            target.heal(self.magnitude)
        elif self.type == 'take_damage':
            target.take_damage(self.magnitude)
    '''add additional types as needed''' 

def mouseEvents():
    print('mouseEvents test')