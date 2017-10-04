'''
Lab 07 - Password Generator
With user input
'''

import random # import random module
import string # import string module

pass_length = input(int(("How long do you want the password to be? "))) # prompt for how long password should be

pass_chars = string.ascii_letters + string.digits # set pass_chars as all letters and digits

for i in range(pass_length): # run as many times as asked
    print(random.choice(pass_chars), end="") # randomly output one of the characters in pass_chars
print("\n")
