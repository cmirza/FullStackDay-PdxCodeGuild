'''
Lab 14 - Practice Problems
Problem 1: Return the number of letter occourances in a string.
'''

word = 'Antidisestablishmentterianism'  # define word var
char = 'i'  # define char var

count = 0  # define char count

for i in word:  # start for loop
    if char == i:  # if char is found in word, iterate count
        count += 1

print(count)  # print count
