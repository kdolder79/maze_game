import adventure_game.my_utils as utils
from colorama import Fore, Style
room2_inventory = {
    'gold key':1,
    'cup':1,
    'pumpkin':1,
    'flashlight':1

}

room1_state = {
    'door locked':False
}

room4_state = {
    'door locked':True
}

description = '''
    . . . Room 2 . . .
    You are in a brightly lit room.
    The room appears to be an office.
    There is a desk in the middle of the room. 
    On the desk you see a small carved pumpkin, a cup, and a flashlight.
    The rest of the room is empty. 
    How strange?
    
    '''
# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    utils.print_description(description)
    # valid commands for this room
    commands = ["go", "take", "drop", "use", 'status']
    no_args = ["status"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]


        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            elif direction == 'south':
                is_locked = room4_state['door locked']
                if not is_locked:
                    next_room = 4
                    done_with_room = True
                elif is_locked:
                    print("The door to room 4 is locked.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go", direction)

        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory,room2_inventory,take_what)

        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory, drop_what)

        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room2_inventory)

        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                object = use_what.split()
                if object[1] == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?',['north','south'])
                    if direction.lower() == 'north':
                        print('The door was already unlocked')
                    elif direction.lower() == 'south':
                        door_locked = room4_state['door locked']
                        if door_locked:
                            if object[0] == 'brass':
                                room4_state['door locked'] = False
                                current_count = player_inventory['brass key']
                                player_inventory['brass key'] = current_count - 1
                                print('The door to the SOUTH is now unlocked.')
                            else:
                                print('A', use_what, 'is unable to unlock the', direction, 'door.')
                        else:
                            print('The door was already unlocked.')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        elif the_command == 'examine':
            examine_what = response[1]


        else:
            print("Command not implemented in ROOM 2,", the_command)

    # end of main while loop
    return next_room

