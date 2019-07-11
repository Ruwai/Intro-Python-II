lfrom room import Room
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

#
# Items
#
room['foyer'].add_item(Item('torch', 'Light up your night in the darkness with no light'))
room['foyer'].add_item(Item('empty-bag', 'Like a plastic bag drifting through the wind...'))
room['overlook'].add_item(Item('shovel', 'I\'ll dig you out of any situation, you are mine until the end of time'))
room['narrow'].add_item(Item('incense', 'Wonder what this is doing here. In a place so narrow as narrow deep.'))
room['treasure'].add_item(Item('box', 'Fill it with the memories of you and me together in a place where we might go insane'))
room['treasure'].add_item(Item('blanket', 'Wrap me around you like a burrito'))
room['treasure'].add_item(Item('ukele', 'My love you used to play the ukele so often, but now you\'re 6 feet under in a coffin'))
#
# Main
#
def validate_cmd(cmd):
    valid_cmds = ['n', 's', 'e', 'w', 'q', 'i', 'inventory']

    split_cmd = cmd.split()
    cmd_len = len(split_cmd)

    if cmd_len != 1 and cmd_len != 2:
        return False

    if cmd_len == 1:
        if split_cmd[0] not in valid_cmds:
            return False

    if cmd_len == 2:
        if split_cmd[0] != 'take' and split_cmd[0] != 'drop':
            return False

    return True

def process_cmd(cmd, player):
    split_cmd = cmd.split()
    cmd_len = len(split_cmd)

    if cmd_len == 1:

        if split_cmd[0] == 'q':
            print('\nLater skater.')
            exit()
        elif split_cmd[0] == 'i' or split_cmd[0] == 'inventory':
            player.print_items_info()
        else:
            if player.move_in_dir(cmd.lower()):
                player.print_room_info()
            else:
                print('\nNot a valid direction')
    else:
        if split_cmd[0] == 'take':
            if player.take_item(split_cmd[1]):
                print(f'\nYou have taken {split_cmd[1]}')
                print(f'\n{player.get_current_room().available_items()}')
            else:
                print('\nItem mentioned not available in room.')
                print(f'\n{player.get_current_room().available_items()}')
        else:
            if player.drop_item(split_cmd[1]):
                print(f'\nYou have dropped {split_cmd[1]}')
            else:
                print('\nItem mentioned not available with you.')

def print_error():
    print('Input invalid.\n')
    print('n - Move North')
    print('s - Move South')
    print('e - Move East')
    print('w - Move West')
    print('\nq - For exiting the game')
    print('\nTake item from current room')
    print('\ntake `item_name`')
    print('\nDrop item in current room')
    print('\ndrop `item_name`')


# Make a new player object that is currently in the 'outside' room.
player = Player('Larry the Lobster')
player.set_current_room(room['outside'])
player.print_room_info()

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

while True:

    cmd = input("\nINPUT COMMAND HERE: ")

    if not validate_cmd(cmd):
        print_error()
        continue

    process_cmd(cmd, player)