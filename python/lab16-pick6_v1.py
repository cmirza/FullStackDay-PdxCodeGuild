'''
Lab 15 - Pick6
'''

import random  # import random module

payout = 0  # define payout var
matches = 0  # define number of matches var
plays = 0  # define number of plays var

chosen_numbers = []  # define list of chosen numbers
for comp_nums in range(5):  # randomly choose 6 numbers
    chosen_numbers.append(random.randint(1, 99))  # choose random number between 1 and 99 and add it to list of chosen numbers

for plays in range (100000):  # run game 100,000 times
    played_numbers = []  # define list of played numbers
    for user_nums in range(5):  # randomly choose 6 numbers
        played_numbers.append(random.randint(1, 99))  # choose random number between 1 and 99 and add it to list of played numbers
    matches = len(set(chosen_numbers) & set(played_numbers))  # compare list of chosen numbers against list of played numbers
    if matches == 0:  # if 0 matches, 0 payout
        payout += 0
    if matches == 1:  # if 1 matches, 4 payout
        payout += 4
    if matches == 2:  # if 2 matches, 7 payout
        payout += 7
    if matches == 3:  # if 3 matches, 100 payout
        payout += 100
    if matches == 4:
        payout += 50000  # if 4 matches, 50000 payout
    if matches == 5:
        payout += 1000000  # if 5 matches, 1000000 payout
    if matches == 6:
        payout += 25000000  # if 6 matches, 25000000 payout
    plays += 1  # iterate number of plays

expenses = plays*2  # expenses are number of plays * $2

print("You made $"+str(payout-expenses)+" playing Powerball\n")  # print out payout minus expenses
