'''
Random string password generator with user input
'''

import random
import string

pass_length = input("How long do you want the password to be? ")
pass_length = int(pass_length)

pass_chars = string.ascii_letters + string.digits

for i in range(pass_length):
    print(random.choice(pass_chars), end="")
print("\n")
