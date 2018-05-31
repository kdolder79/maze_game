import adventure_game.my_utils as utils
from colorama import Fore, Style
# # # # #
# ROOM 9
#
# Serves as a good template for blank rooms
room9_description = '''
    . . .  9th room ... 
    A kitchen/break room. Well kinda.
    It looks as if it was ransacked. 
    Drawers are pulled out with nothing left inside them. 
    No silverware, dishes, or food. 
    The chairs are all scattered throughout this room.
    
     '''

room8_state = {
    'door locked': False
}


room9_inventory = {
    'sword': 1,
    'bronze key': 1
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    utils.print_description(room9_description)


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
            if go_where == 'south':
                is_locked = room8_state['door locked']
                if not is_locked:
                    next_room = 8
                    done_with_room = True
                else:
                    print('The door to Room 8 is locked.')
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room9_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room9_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                if use_what == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?', ['south'])
                    if direction.lower() == 'south':
                        print('The door was already unlocked')

                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print('The command:', the_command, 'has not been implemented in room 9.')


            # END of WHILE LOOP
    return next_room
