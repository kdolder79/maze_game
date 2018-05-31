import adventure_game.my_utils as utils
from colorama import Fore, Style
# # # # #
# ROOM 11
#
# Serves as a good template for blank rooms
room11_description = '''
    . . .  11th room ... 
    It looks like the end of the hallway. 
    How peculiar? A hallway to nothing. 
    There is quite a lot of junk here. 


     '''

room10_state = {
    'door locked': False
}

room11_inventory = {
    'sword': 1,
    'wood key': 1,
    'granola bar wrapper':1,
    'cardboard box':3,
    'plastic water bottle':4
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    utils.print_description(room11_description)


    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status"]
    no_args = ["status"]

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
                is_locked = room10_state['door locked']
                if not is_locked:
                    next_room = 10
                    done_with_room = True
                else:
                    print('The door to Room 10 is locked.')
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room11_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room11_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                if use_what == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?', ['north'])
                    if direction.lower() == 'north':
                        door_locked = room10_state['door locked']
                        if door_locked:
                            room10_state['door locked'] = False
                            current_count = player_inventory['key']
                            player_inventory['key'] = current_count - 1
                            print('The door to the NORTH is now unlocked.')
                        else:
                            print('The door was already unlocked')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print('The command:', the_command, 'has not been implemented in room 8.')


            # END of WHILE LOOP
    return next_room
