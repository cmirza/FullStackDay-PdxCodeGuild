'''
Lab 22 - Practice Problems
Problem 14: Return the letter that appears the latest in the english alphabet.
'''


# Latest letter function - Lowercase all chars in word. Set latest char to a (smallest value). Loop through characters
# in word. If unicode value of current character is greater than unicode value of latest character, set current
# character to latest character, otherwise continue looping. When done, return latest character.
def latest_letter(word):
    word = word.lower()
    latest_char = 'a'
    for char in word:
        if ord(char) > ord(latest_char):
            latest_char = char
        else:
            continue
    return 'The latest letter is ' + latest_char + '.'


# prompt for length of Fibonacci sequence wanted
input_word = input("Enter a word (the longer the better): ")

# Pass input number to function and print result
print(latest_letter(input_word))
