import json

class Inventory:
    def __init__(self):

        self.inventory = []
        
    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def calculate_total_weight(self):
        total_weight = 0
        for item in self.inventory:
            total_weight += item['weight']
        print(total_weight)

    def calculate_total_value(self):
        total_value = 0
        for item in self.inventory:
            total_value += (item['value'] + (item['durability'] /2))
        print(total_value)

    def get_item_details(self, item):
        item.display_info()

    def display_inventory(self):
        for item in self.inventory:
            print(item)