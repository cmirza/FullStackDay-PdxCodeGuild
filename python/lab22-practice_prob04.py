'''
Lab 22 - Practice Problems
Problem 4: Get a string from the user, print out another string, doubling every letter.
'''


def char_doublr(input):  # define character doubler function

    input_double = ""  # define string for doubled output
    for i in range(len(input)):  # start loop for length of chars in string
        input_double += input[i]*2  # add each character in input to input double, twice
    return input_double  # return doubled string


my_input = input('Enter some text: ')  # prompt user to enter some text

print(char_doublr(my_input))  # pass input to function and print result
