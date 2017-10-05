'''
Lab 13 - Guess the Number
With 'too high' and 'too low'
'''

import random  # import random module

play_count = 0  # play counter
previous_guess = 0  # define previous guess var
chosen_number = random.randint(1, 10)  # choose random number between 1 and 10

while True:  # begin input loop
    play_count += 1  # iterate play count
    number_guess = input('Guess a number between 1 and 10.\n')  # prompt to guess a number
    if number_guess == "done":  # if user ends game
        print("Goodbye!")
        break
    if int(number_guess) == chosen_number:  # if correct guess end game
        print("Correct! The number was", chosen_number,". It took you", play_count, "guesses.")
        break
    if abs(int(number_guess) - chosen_number) > abs(previous_guess - chosen_number):  # if guess is colder
        print("You're getting colder.")
    if abs(int(number_guess) - chosen_number) < abs(previous_guess - chosen_number):  # if guess is warmer
        print("You're getting warmer.")
    previous_guess = int(number_guess)  # assign current guess to previous guess var
