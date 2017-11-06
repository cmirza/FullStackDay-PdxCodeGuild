'''
Lab 14 - Practice Problems
Problem 3: Write a function that tells whether a number is even or odd.
'''


def is_even(x):  # define function
    if x % 2 != 0:  # if number has a remainder when divided by two it is odd
        return False
    else:  # otherwise it is even
        return True


number = input("Enter a number: ")  # prompt for a number
number = int(number)  # convert input to int

if number == 0:  # if function returns false, print false
    print("False")
else:  # otherwise print even
    print("True")
