'''
Magic Eight Ball
'''

import random

magic_responses = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "My reply is no."]

magic_question = input("Ask the Magic Ball anything!\n")

magic_answer = random.choice(magic_responses)

print(magic_answer)
