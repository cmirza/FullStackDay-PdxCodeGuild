'''
Lab 07 - Password Generator
'''

import random # import random module
import string # import string module

pass_chars = string.ascii_letters + string.digits # set pass_chars as all letters and digits

for i in range(14): # run 14 times
    print(random.choice(pass_chars), end="") # randomly output one of the characters in pass_chars
print("\n") # print a new line
