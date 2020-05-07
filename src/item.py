
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}, {self.description}"

soccer_ball = Item("soccer ball", "a ball that is white with black hexagon spots on it ")

print(soccer_ball)