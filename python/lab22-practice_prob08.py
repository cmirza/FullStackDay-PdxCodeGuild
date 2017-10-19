'''
Lab 22 - Practice Problems
Problem 8: Write a function that takes a string, and returns a list of strings, each missing a different character.
'''


# Missing character function - Define list for words with missing chars. Loop through the length of the word. Slice
# the chars around the character to remove, concatenate the two parts as a new word, then append to list of words and
# iterate. When loop is done, return word list.
def missing_char(word):
    word_list = []
    i = 0
    while i <= len(word)-1:
        new_word = word[:int(i)] + word[(int(i) + 1):]
        word_list.append(new_word)
        i += 1
    return word_list


# Prompt for a word.
input_word = input("Enter a word: ")

# Pass input word to function and print result
print(missing_char(input_word))
