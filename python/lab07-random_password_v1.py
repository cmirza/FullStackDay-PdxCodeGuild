'''
Random string password generator
'''

import random
import string

pass_chars = string.ascii_letters + string.digits

for i in range(14):
    print(random.choice(pass_chars), end="")
print("\n")
