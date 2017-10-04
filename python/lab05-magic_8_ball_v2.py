'''
Lab 05 - Magic 8-Ball
With while loop
'''

import random # import random module

play = True # set default state of game

while play: # begin while loop

    magic_responses = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "My reply is no."]  # define possible responses in list array

    magic_question = input("Ask the Magic Ball anything!\n") # prompt for question

    print(random.choice(magic_responses)) # print one of the responses at random

    play_again = str(input("Would you like to play again? Type yes or no: ")) # prompt to play again
    play_again = play_again.lower() # make input lower case
    if play_again == "no": # if input is 'no' end game
        play = False
