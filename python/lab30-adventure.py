'''
Lab 30 - Adventure
• use more succinct commands (l/u/d/r)
• add boundaries to the map, when the player attempts to move beyond the boundary, stop them
'''

import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'l':
        if player_j < 1:  # catch if player tries to go beyond left boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_j -= 1  # move left
    elif command == 'r':
        if player_j > 8:   # catch if player tries to go beyond right boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_j += 1  # move right
    elif command == 'u':
        if player_i < 1:   # catch if player tries to go beyond top boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_i -= 1  # move up
    elif command == 'd':
        if player_i > 8:    # catch if player tries to go beyond bottom boundary of board
            print('you\'ve reached the end of this world!')
            pass
        else:
            player_i += 1  # move down

    # check if the player is has reached the boundary of the map


    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break



            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
    print(player_i, player_j)
