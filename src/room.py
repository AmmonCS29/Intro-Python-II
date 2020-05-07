# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    
    def __str__(self):
        return f"you are in the {self.name}, {self.description} "


    def on_drop(self, item):
        self.items.append(item)
        print(f"\n{item.name} was added to the room \n")
    
    def on_take(self, item):
        self.items.remove(item)
        print(f"you have picked up {item.name} \n")
    

# Testing functions
# outside = Room('outside', 'the caves forward the cliff is backward')
# sword = Item('sword', 'black and yellow')
# outside.add_item(sword)

# for obj in outside.items:
#     print(obj.name, obj.description)



