# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def __str__(self):
        return f"Your name is {self.name}, and you are {self.current_room}"
    
    def add_inventory(self, item):
        self.inventory.append(item)
        print(f"\n{item.name} was added to your inventory \n")

    def remove_inventory(self, item):
        self.inventory.remove(item)
        print(f"{item.name} was removed from your inventory \n")
    
        
# player1 = Player("Arash", "outside")


# print(player1)