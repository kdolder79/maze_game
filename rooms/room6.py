import adventure_game.my_utils as utils
from colorama import Fore, Style
# # # # #
# ROOM 6
#
# Serves as a good template for blank rooms
room6_description = '''
    . . .  6th room ... 
    Turning the corner from the past room you see that you've made it to a hallway.
    There is a closed door at the end of this hallway. 

     '''

room5_state = {
    'door locked': False
}
room7_state = {
    'door locked': True
}

room6_inventory = {
    'small potted plant': 1,

}


def run_room(player_inventory):
    # Let the user know what the room looks like
    utils.print_description(room6_description)


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
                next_room = 5
                done_with_room = True
            elif go_where == 'east':
                is_locked = room7_state['door locked']
                if not is_locked:
                    next_room = 7
                    done_with_room = True
                else:
                    print('The door to Room 7 is locked.')
            else:
                print('You cannot go:', go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room6_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room6_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room6_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                object = use_what.split()
                if object[1] == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?', ['north', 'east'])
                    if direction.lower() == 'north':
                        print('The door was already unlocked')
                    elif direction.lower() == 'east':
                        door_locked = room7_state['door locked']
                        if door_locked:
                            if object[0] == 'silver':
                                room7_state['door locked'] = False
                                current_count = player_inventory['silver key']
                                player_inventory['silver key'] = current_count - 1
                                print('The door to the EAST is now unlocked.')
                            else:
                                print('A', use_what, 'is unable to unlock the', direction, 'door.')
                        else:
                            print('The door was already unlocked.')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print('The command:', the_command, 'has not been implemented in room 6.')


            # END of WHILE LOOP
    return next_room
