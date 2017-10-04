'''
Lab 06 - Random Emoticon Generator
With while loop
'''

import random # import random module

eyes = [":",";","#"] # define eyes in list array
noses = ["-","^","*"] # define noses in list array
mouths = [")","(","|"] # define mouths in list array

i = 0 # set iteration to zero

while i < 5: # run five times
    print(random.choice(eyes)+random.choice(noses)+random.choice(mouths))  # randomly choose eyes, nose and mouth, concatenate and print
    i=i+1 # iterate by one
