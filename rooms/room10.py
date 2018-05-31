import adventure_game.my_utils as utils
from colorama import Fore, Style
# # # # #
# ROOM 10
#
# Serves as a good template for blank rooms
room10_description = '''
    . . .  10th room ... 
    This looks like another hallway.
    Not much is in this room.

     '''

room8_state = {
    'door locked': False
}
room11_state = {
    'door locked': True
}

room10_inventory = {
    'sword': 1,
    'iron key': 1
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    utils.print_description(room10_description)


    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'north':
                is_locked = room8_state['door locked']
                if not is_locked:
                    next_room = 8
                    done_with_room = True
                else:
                    print('The door to Room 8 is locked.')
            elif go_where == 'south':
                is_locked = room11_state['door locked']
                if not is_locked:
                    next_room = 11
                    done_with_room = True
                else:
                    print('The door to Room 11 is locked.')
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room10_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room10_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room10_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                object = use_what.split()
                if object[1] == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?', ['north', 'south'])
                    if direction.lower() == 'north':
                        print('The door was already unlocked')
                    elif direction.lower() == 'south':
                        door_locked = room11_state['door locked']
                        if door_locked:
                            if object[0] == 'iron':
                                room11_state['door locked'] = False
                                current_count = player_inventory['iron key']
                                player_inventory['iron key'] = current_count - 1
                                print('The door to the SOUTH is now unlocked.')
                            else:
                                print('A', use_what, 'is unable to unlock the', direction, 'door.')
                        else:
                            print('The door was already unlocked.')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print('The command:', the_command, 'has not been implemented in room 10.')


            # END of WHILE LOOP
    return next_room
