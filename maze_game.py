# fix to run program from our directory
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+'/./../')


# room imports
import adventure_game.rooms.room1 as r1
import adventure_game.rooms.room2 as r2
import adventure_game.rooms.room3 as r3
import adventure_game.rooms.room4 as r4
import adventure_game.rooms.room5 as r5
import adventure_game.rooms.room6 as r6
import adventure_game.rooms.room7 as r7
import adventure_game.rooms.room8 as r8
import adventure_game.rooms.room9 as r9
import adventure_game.rooms.room10 as r10
import adventure_game.rooms.room11 as r11

#required to use colorama
from colorama import init
init()

# Default the player to the first room
room_number = 1

# Player Inventory5
player_inventory = {
    'torch': 1,
    'cup':0,
    'pumpkin':0
}

print("Welcome to the maze game...\n")

should_continue = True

while should_continue:
    if room_number == 1:
        room_number = r1.run_room( player_inventory )
    elif room_number == 2:
        room_number = r2.run_room( player_inventory )
    elif room_number == 3:
        room_number = r3.run_room( player_inventory )
    elif room_number == 4:
        room_number = r4.run_room( player_inventory )
    elif room_number == 5:
        room_number = r5.run_room( player_inventory )
    elif room_number == 6:
        room_number = r6.run_room( player_inventory )
    elif room_number == 7:
        room_number = r7.run_room( player_inventory )
    elif room_number == 8:
        room_number = r8.run_room( player_inventory )
    elif room_number == 9:
        room_number = r9.run_room( player_inventory )
    elif room_number == 10:
        room_number = r10.run_room( player_inventory )
    elif room_number == 11:
        room_number = r11.run_room( player_inventory )
    elif room_number == 0:
        print('You have successfully beat the game!')
        exit()
    else:
        print("Ack I don't know room number:", room_number)
        break




print("The game has ended...")



#TEST EXIT CODE FOR ENDING THE GAME AFTER ROOM THREE