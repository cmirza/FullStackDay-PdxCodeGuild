'''
Lab 15 - Pick6
'''

import random  # import random module

payout = 0
matches = 0
plays = 0

chosen_numbers = []
for comp_nums in range(5):
    chosen_numbers.append(random.randint(1, 99))  # choose random number between 1 and 99

for plays in range (100000):
    played_numbers = []
    for user_nums in range(5):
        played_numbers.append(random.randint(1, 99))  # choose random number between 1 and 99
    matches = len(set(chosen_numbers) & set(played_numbers))
    if matches == 0:
        payout += 0
    if matches == 1:
        payout += 4
    if matches == 2:
        payout += 7
    if matches == 3:
        payout += 100
    if matches == 4:
        payout += 50000
    if matches == 5:
        payout += 1000000
    if matches == 6:
        payout += 25000000
    plays += 1

print("You made $"+str(payout-(plays*2))+" playing Powerball")
