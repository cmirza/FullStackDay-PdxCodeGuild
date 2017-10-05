'''
Lab 13 - Guess the Number
With 'too high' and 'too low'
'''

import random  # import random module

play_count = 0  # play counter
chosen_number = random.randint(1, 10)  # choose random number between 1 and 10

while True:  # begin input loop
    play_count += 1  # iterate play count
    number_guess = int(input('Guess a number between 1 and 10.\n'))  # prompt to guess a number
    if number_guess > chosen_number:  # check if number is too high and prompt
        print("Too high!")
    if number_guess < chosen_number:  # check if number is too low and prompt
        print("Too low.")
    if number_guess == chosen_number:  # if correct guess end game
        print("Correct! The number was", chosen_number,". It took you", play_count, "guesses.")
        break
    elif number_guess == "done":  # if user ends game
        print("You made", play_count, "guesses.")
        break
