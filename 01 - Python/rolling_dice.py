import time
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_d20():
    r = 0
    n_rolls = random.randint(20, 40)
    for i in range(n_rolls):
        time.sleep(i*i/10000)
        r = random.randint(1, 20)
        cls()
        print(r)

    return r

print(roll_d20())