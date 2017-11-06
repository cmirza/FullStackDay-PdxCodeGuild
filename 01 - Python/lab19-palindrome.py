'''
Lab 19 - Palindrome
'''


def palindrome(word):  #define reverse funcion
    rev_word = []  # define reverse list
    for i in word:  # start for loop
        rev_word.insert(0, i)  # use insert method to insert each letter in sequence into the 0 position of reversed list
    if word == rev_word:  # if word list match reversed word list, return positive
        return "Yes, it is."
    else:  # otherwise return negative
        return "No, it is not."


word = input('Enter a word you think might be a palindrome: ')  # request for word that might be a palindrome
word = list(word)  # convert string into list

print(palindrome(word))  # pass list to function and print result
