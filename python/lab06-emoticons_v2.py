'''
Emoticon generator with while loop
'''

import random

eyes = [":",";","#"]
noses = ["-","^","*"]
mouths = [")","(","|"]

i = 0

while i < 5:
    print(random.choice(eyes)+random.choice(noses)+random.choice(mouths))
    i=i+1
