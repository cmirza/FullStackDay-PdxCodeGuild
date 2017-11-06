'''
Lab 08 - Rock Paper Scissors
'''

import random # import random module

valid_choice = ('rock','paper','scissor') # define valid choices

computer_choice = random.choice(valid_choice) # computer chooses a valid choice at random

user_choice = input("Rock, Paper or Scissor?\n") # prompt user for a choice
user_choice = user_choice.lower() # set input to lower case

if user_choice == "rock": # if user picks rock...
    if computer_choice == "rock": # and computer picks rock, its a tie
        print("Rock, it's a tie.")
    elif computer_choice == "paper": # and computer picks paper, user looses
        print("Paper, you loose.")
    elif computer_choice == "scissor": # and computer picks scissor, user wins
        print("Scissor, you win!")

if user_choice == "paper": # if user picks paper...
    if computer_choice == "rock": # and computer picks rock, user wins
        print("Rock, you win!")
    elif computer_choice == "paper": # and computer picks paper, its a tie
        print("Paper, it's a tie.")
    elif computer_choice == "scissor": # and computer picks scissor, user looses
        print("Scissor, you loose.")

if user_choice == "scissor": # if user picks scissor...
    if computer_choice == "rock": # and computer picks rock, user looses
        print("Rock, you loose.")
    elif computer_choice == "paper": # and computer picks paper, user wins
        print("Paper, you win!")
    elif computer_choice == "scissor": # and computer picks scissor, its a tie
        print("Scissor, it's a tie.")

elif user_choice not in valid_choice: # if input isn't a valid choice, give an error
    print("Invalid choice.\n")