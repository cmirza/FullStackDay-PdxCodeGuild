'''
Lab 22 - Practice Problems
Problem 2: Print out every other element of a list, first using a while loop, then using a for loop.
'''


def print_every_other(num):
    for i in range(0, len(num), 2):
        return num[i]


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print_every_other(nums)
