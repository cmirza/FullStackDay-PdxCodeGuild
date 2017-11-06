'''
drop dead - dice game
'''

import random

# create dice, number of players, roll all 5 dice
# if any dice are 2 & 5, the whole roll is dead
# and those dice are discarded until the player has
# no dice left to roll.
# go through all of the players, and the player
# with the highest score wins.


class Dice:

    def __init__(self):
        self.alive = True

    def roll(self):
        return random.randint(1, 6)


dice = []

for i in range(5):
    dice.append(Die())

for i in range(len(dice)):
    print(dice[i].roll())

num_players = int(input('How many players? '))

player_score = []
player_dice = []


for i in range(num_players):
    print(f'player {i}\'s turn')
    player_dice.extend(dice)
    player_score.append(0)
    while len(player_dice) > 0:

        for i in range(num_players):
            player_dice.extend(dice)
            player_score.append(0)
            for j in range(len(player_dice)):
                die_0 = player_dice[j].roll()
                if die_0 in (2,5):

