'''
Lab 05 - Magic 8-Ball
'''

import random # import random module

magic_responses = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "My reply is no."] # define possible responses in list array

magic_question = input("Ask the Magic Ball anything!\n") # prompt for question

print(random.choice(magic_responses)) # print one of the responses at random
