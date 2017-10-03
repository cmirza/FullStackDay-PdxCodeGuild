'''
Magic Eight Ball with while loop
'''

import random

play = True

while play:

    magic_responses = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "My reply is no."]

    magic_question = input("Ask the Magic Ball anything!\n")

    magic_answer = random.choice(magic_responses)

    print(magic_answer)

    play_again = str(input("Would you like to play again? Type yes or no: "))
    play_again = play_again.lower()
    if play_again == "no":
        play = False
