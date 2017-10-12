'''
Lab 22 - Practice Problems
Problem 4: Get a string from the user, print out another string, doubling every letter.
'''


def char_doublr(input):

    input_double = ""
    for i in range (len(input)):
        input_double += input[i]*2
    print(input_double)


my_input = input('Enter some text: ')

char_doublr(my_input)
