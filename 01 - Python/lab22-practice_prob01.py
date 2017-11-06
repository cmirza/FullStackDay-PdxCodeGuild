'''
Lab 22 - Practice Problems
Problem 1: Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
'''


my_list = []
while True:
    my_input = input('Enter a number (or \'done\'): ')
    if my_input == 'done':
        print(my_list)
        break
    my_list.append(int(my_input))

