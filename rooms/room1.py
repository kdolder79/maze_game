import adventure_game.my_utils as utils
from colorama import Fore, Style
room1_inventory = {
    'pumpkin':1,
    'flashlight':1,
    'brass key':1,
    'crumpled up paper':5
}

room3_state = {
    'door locked':True
}
room2_state = {
    'door locked':False
}

description = '''
    . . . Main Room . . .
    You wake up. 
    You're lying on the floor.
    Why are you on the floor?

    You get up and see that you're in an office.
    The lights flicker constantly. 
    How spooky.
    
    You see there are words all over the walls writen in a deep red color.
    
    "I have offered you this chilling challenge. Find a way out. Keys are scattered throughout the building. Good Luck."

    '''

def run_room(player_inventory):
    utils.print_description(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status"]
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
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                is_locked = room3_state['door locked']
                if not is_locked:
                    next_room = 3
                    done_with_room = True
                else:
                    print('The door to Room 3 is locked.')
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory,room1_inventory,take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room1_inventory, drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room1_inventory)
        elif the_command == 'examine':
            examine_what = response[1]
            print('')
        elif the_command == 'use':
            use_what = response[1]
            if use_what in player_inventory:
                object = use_what.split()
                if object[1] == 'key':
                    direction = utils.prompt_question('Which door would you like to use the key on?',['east','south'])
                    if direction.lower() == 'east':
                        door_locked = room3_state['door locked']
                        if door_locked:
                            if object[0] == 'wood':
                                room3_state['door locked'] = False
                                current_count = player_inventory['wood key']
                                player_inventory['wood key'] = current_count - 1
                                print('The door to the EAST is now unlocked.')
                            else:
                                print('A', use_what, 'is unable to unlock the', direction, 'door.')
                        else:
                            print('The door was already unlocked')
                    elif direction.lower() == 'south':
                        print('The door was already unlocked.')
                else:
                    print('You have no way to use:', use_what)
            else:
                print("You don't have:", use_what)
        else:
            print("Command not implemented in ROOM 1,", the_command)

    # end of while loop
    return next_room
