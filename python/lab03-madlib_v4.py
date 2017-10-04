'''
Lab 03 - Mad Libs
Using split function and random module
Repeatable game with while loop
'''

import random # import random module

play = True # set default state of game

while play: # begin while loop

    adjective1 = input("Give me an adjective:\n") # prompt for adjective

    input_noun = input("Give me two nouns separated by commas:\n") # prompt for two nouns separated by comma
    input_noun.split(", ") # define comma as split point
    noun1, noun3 = input_noun.split(", ") # use split function on the string
    noun = [noun1, noun3] # place nouns into list array

    noun2 = input("Give me a plural noun:\n") # prompt for noun
    verb1 = input("Give me a verb ending in 'ed':\n") # prompt for verb

    print(" There was a " + adjective1 + " woman who lived in a " + random.choice(noun) + ".\n She had so many " + noun2 + " she didnt know what to do.\n She gave them some broth without any " + random.choice(noun) + ".\n She " + verb1 + " them all soundly and put them to bed.\n") # print story

    play_again = str(input("Would you like to make another story? Type 'yes' or 'no': ")) # prompt to play again
    play_again = play_again.lower() # make input lower case
    if play_again == "no": # if input is 'no' end game
        play = False
