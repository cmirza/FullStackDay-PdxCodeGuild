'''
Lab 19 - Anagram
'''


def anagram(anag_1, anag_2):  # define anagram function
    anags_1 = sorted(anag_1)  # sort first anagram chars alphabetically
    anags_2 = sorted(anag_2)  # sort second anagram chars alphabetically
    anags_1 = ''.join(anags_1)  # turn list back into string
    anags_2 = ''.join(anags_2)  # turn list back into string
    anags_1 = anags_1.lower()  # lower all chars
    anags_2 = anags_2.lower()  # lower all chard
    anags_1 = anags_1.replace(' ', '')  # remove whitespace
    anags_2 = anags_2.replace(' ', '')  # remove whitespace
    if anags_1 == anags_2:  # if anagrams match, return positive
        return anag_1 + " and " + anag_2 + " are anagrams."
    else:  # otherwise return negative
        return anag_1 + " and " + anag_2 + " are not anagrams."

word_1 = input('Enter the first word: \n')  # prompt for first word
word_2 = input('Enter the second word: \n')  # prompt for second word

print(anagram(word_1, word_2))  # pass list to function and print result
