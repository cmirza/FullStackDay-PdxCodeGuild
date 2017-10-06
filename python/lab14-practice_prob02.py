'''
Lab 14 - Practice Problems
Problem 2: Convert input strings to lowercase without any surrounding whitespace.
'''

input_string = input("Enter a string: ")  # prompt for a string

input_string = input_string.replace(" ", "")  # remove all spaces
input_string = input_string.lower()  # lowercase all chars

print(input_string)  # output modified string
