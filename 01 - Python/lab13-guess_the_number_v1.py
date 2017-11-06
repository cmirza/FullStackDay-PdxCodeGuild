'''
Lab 13 - Guess the Number
'''

import random  # import random module

play_count = 0  # play counter
chosen_number = random.randint(1, 10)  # choose random number between 1 and 10

while True:  # begin input loop
    play_count += 1  # iterate play count
    number_guess = int(input('Guess a number between 1 and 10.\n'))  # prompt to guess a number
    if number_guess != chosen_number:  # if wrong guess prompt to try again
        print("Sorry, try again.")
    if number_guess == chosen_number:  # if correct guess end game
        print("Correct! The number was", chosen_number)
        break
    elif play_count == 10:  # if guesses exhausted end game
        print("Sorry! The number was", number_guess)
        break
