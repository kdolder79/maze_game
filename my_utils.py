import time
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        print('Your choices are:', valid_options)
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False;
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#has_a command
#   has_a will check whether por not a dictionary has the item specified
#   check that the count is greater than zero
#
def has_a (player_inventory, item):
    if item in player_inventory.keys():
        count = player_inventory[item]
        if count > 0:
            return True
        else:
            return False
    else:
        return False


#end of has_a

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#drop_item
#   will lose whatever you drop and it'll add to room inventory
#
def drop_item (player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        current_count = player_inventory[item]
        player_inventory[item] = current_count-1

        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count+1
        else:
            room_inventory[item] = 1
        print('You dropped the', item)

    else:
        print('You cannot drop something that you do not have.')

#end of drop_item

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#take_item
#   remove item from room inventory and add it to player inventory
#
def take_item (player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        current_count = room_inventory[item]
        room_inventory[item] = current_count-1

        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count+1
        else:
            player_inventory[item] = 1
        print('You took the', item)
    else:
        print('You cannot take something that does not exist in this room.')

#end of take_item

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#
#room_status
#   check what room has
#


def room_status (room_inventory):
    print('\tIn the room you see:')
    nothing = True
    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            nothing = False
            print("\t\t", key)
    if nothing == True:
        print('\t . . . sadly, nothing.')

#end of room_status

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#player_status
#   check player status
#

def player_status (player_inventory):
    print('\t You currently possess:')
    nothing = True
    for key in player_inventory.keys():
        if player_inventory[key]>0:
            nothing = False
            print('\t\t', key, ':', player_inventory[key])
    if nothing == True:
        print('\t . . . sadly, nothing')

#end of player_status

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#scrub_response

def scrub_response(dirty_response):
    result = []
    action = dirty_response[0]
    result.append(action)
    if len(dirty_response) >= 2:
        argument = dirty_response[1]
        if len(dirty_response) >=3:
            second = dirty_response[2]
            if action in ['take','drop','use',]:
                if second == 'sword':
                    if argument == 'short':
                        result.append('short sword')
                elif second == 'pick':
                    if argument == 'ice':
                        result.append('ice pick')
                elif second == 'key':
                    if argument == 'brass':
                        result.append('brass key')
                    elif argument == 'gold':
                        result.append('gold key')
                    elif argument == 'silver':
                        result.append('silver key')
                    elif argument == 'antique':
                        result.append('antique key')
                    elif argument == 'bronze':
                        result.append('bronze key')
                    elif argument == 'iron':
                        result.append('iron key')
                    elif argument == 'wood':
                        result.append('wood key')
                else:
                    result.append(argument)
        else:
            result.append(argument)

    return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#print description line by line

def print_description (description):
    lines = description.split('\n')
    for line in lines:
        print(line)
        time.sleep(.01)

