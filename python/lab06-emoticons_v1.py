'''
Lab 06 - Random Emoticon Generator
'''

import random # import random module

eyes = [":",";","#"] # define eyes in list array
noses = ["-","^","*"] # define noses in list array
mouths = [")","(","|"] # define mouths in list array

print(random.choice(eyes)+random.choice(noses)+random.choice(mouths)) # randomly choose eyes, nose and mouth, concatenate and print
