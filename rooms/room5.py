import adventure_game.my_utils as utils
from colorama import Fore, Style
# # # # #
# ROOM 5
#
# Serves as a good template for blank rooms
room5_description = '''
    . . .  5th room ... 
    This is an office. 
    It seems to be split with a few workers because there are three different desks in this room.
    There are spooky posters and fake bugs everywhere. 
    This room was most likely decorated for Halloween. 
    
     '''

room4_state = {
    'door locked':False
}
room6_state = {
    'door locked':False
}

room5_inventory = {
    'short sword':1,
    'silver key':1,
    'fake cockroach':5,
    'fake beetle':3
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    utils.print_description(room5_description)

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
            if go_where=='west':
                next_room = 4
                done_with_room = True
            elif go_where=='south':
                is_locked = room6_state['door locked']
                if not is_locked:
                    next_room = 6
                    done_with_room = True
                else:
                    print('The door to Room 6 is locked.')
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room5_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room5_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room5_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                object = use_what.split()
                if object[1] == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?',['west','south'])
                    if direction.lower() == 'west':
                        print('The door was already unlocked')
                    elif direction.lower() == 'south':
                        print('The door was already unlocked.')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print('The command:', the_command, 'has not been implemented in room 5.')


            # END of WHILE LOOP
    return next_room
