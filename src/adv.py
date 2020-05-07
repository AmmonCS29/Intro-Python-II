from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'secret' : Room("Secret Treasure", """a tiny room that has a hidden treasure that will take you to the ship"""),

    'ship' : Room("Pirate Ship", """ I am outside the secret room, take me to find the treasure on the map that you have just found in the secret room """ )

}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['secret']
room['secret'].s_to = room['treasure'] 
room['secret'].e_to = room['ship']

## Items added to rooms

sword = Item("sword", "defending")
axe = Item("axe", "battle axe")
torch = Item("torch", "light me on fire")
dagger = Item("dagger", "Used to kill or hunting")
gold = Item("gold", "You'll be rich forever")
tmap = Item("map", "find the room to the ship")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [dagger]
room['narrow'].items = [axe, sword]
room['treasure'].items = [gold]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Ammon', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# This is for adding color
print("\033[1;32;40m \n")

while True:
    # print(player.current_room)

    action = input('Enter an action: ').split(' ')
    
    #assigning index of input to variable 
    if len(action) == 1:
        for i in action:
            action = i
     
    elif len(action) == 2:
        action_item = action[1]
        action = action[0]

    #  get items  
    if action in ['get', 'take']:
        for i in player.current_room.items:
            if i.name == action_item:
                # action_item = i
                player.current_room.on_take(i)
                player.add_inventory(i)
                print('check inventory')
            else:
                print(f"{action_item} does not exist, look for items in room ")
    
    # drop items
    if action in ['drop', 'd' ]:
        for i in player.inventory:
            if i.name == action_item:
                # action_item = i
                player.current_room.on_drop(i)
                player.remove_inventory(i)        
        else:
            print(f'Cannot drop {action_item}, it is not in your inventory')
                
    # check inventory
    if action in ['inventory', 'i']:
        if len(player.inventory) >= 1:
            for i in player.inventory:
                print(i)
        else:
            print('\ninventory is empty\n')

    # Start the game and directions
    if action == 'start':
        if player.current_room:
            print(f'{player.current_room}')
        else:
            print('\n no path in that direction \n')
    
    if action == 'n':
        if player.current_room.n_to:    
            player.current_room=player.current_room.n_to
            print(f'{player.current_room}')
        else: 
            print('\n you cannot go north \n')
    if action == 's':
        if player.current_room.s_to:
            player.current_room=player.current_room.s_to
            print(f'{player.current_room}')
        else:
            print('\nno path in that direction\n')
    if action == 'e':
        if player.current_room.e_to:
            player.current_room=player.current_room.e_to
            print(f'{player.current_room}')
        else:
            print('\nno path in that direction\n')

    if action == 'w':
        if player.current_room.w_to:
            player.current_room=player.current_room.w_to
            print(f'{player.current_room}')
        else:
            print('\n no path in that direction \n')
    
    if action in ['q', 'quit','exit']:
       exit()
    
    # look for items in the room
    if action == 'look':
        if player.current_room.items:
            for obj in player.current_room.items:    
                print(f'\n{obj.name}\n')
        else:
            print('\nThere are no items in this room\n')

    

    


