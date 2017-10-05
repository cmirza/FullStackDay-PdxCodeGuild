'''
Lab 14 - Practice Problems
Problem x: Return the letter that appears last in the english alphabet.
'''

import string  # import string module

alphabet = string.ascii_lowercase  # define alphabet as all lowercase characters
word = "pneumonoultramicroscopicsilicovolcanoconiosis"  # define word to check
last_word = 0

for i in word:  # iterate through the characters in word
    if alphabet.index(i) > last_word:  # if the value of the char in the alphabet is greater than the last greatest char
        last_word = alphabet.index(i)  # assign it to the last greatest char variable
    else:
        pass  # otherwise skip the char

print("The latest letter is ", alphabet[int(last_word)])  # print the last greatest character
