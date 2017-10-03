'''
Rock, paper, scissor game
'''

import random

valid_choice = ('rock','paper','scissor')

computer_choice = random.choice(valid_choice)

user_choice = input("Rock, Paper or Scissors?\n")
user_choice = user_choice.lower()

if user_choice == "rock":
    if computer_choice == "rock":
        print("Rock, it's a tie.")
    elif computer_choice == "paper":
        print("Paper, you loose.")
    elif computer_choice == "scissor":
        print("Scissor, you win!")

if user_choice == "paper":
    if computer_choice == "rock":
        print("Rock, you win!")
    elif computer_choice == "paper":
        print("Paper, it's a tie.")
    elif computer_choice == "scissor":
        print("Scissor, you loose.")

if user_choice == "scissor":
    if computer_choice == "rock":
        print("Rock, you loose.")
    elif computer_choice == "paper":
        print("Paper, you win!")
    elif computer_choice == "scissor":
        print("Scissor, it's a tie.")

elif user_choice not in valid_choice:
    print("Invalid choice.\n")