'''
Lab 22 - Practice Problems
Problem 9: Write a function that returns the number of occurances of 'hi' in a given string.
'''


# Count hi function - Start counter. Start loop for the range of the length of input string. If the characters starting
# at the iteration and ending two chars (length of 'hi' ahead) match 'hi', iterate counter. When done, return counter
def count_hi(hi_hi):
    counter = 0
    for i in range(len(hi_hi)):
        if hi_hi[i:i + 2] == 'hi':
            counter += 1
    return counter


# Prompt for repeating 'hi's.
input_hi = input("Type 'hihihi...': ")

# Pass input word to function and print result
print(count_hi(input_hi))
