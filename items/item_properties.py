from effects import Effects as effects

class Item:
    def __init__(self, item_dict):
        self.item_dict = item_dict

        self.name = self.item_dict['name']
        self.weight = float(self.item_dict['weight'])
        
        self.value = int(self.item_dict['value'])
        self.id = int(self.item_dict['id'])

        self.description = self.item_dict['description']

    def display_info(self):
        print(self.item_dict)
    def use(self, target):
        # Define the behaviour of the item
        pass

