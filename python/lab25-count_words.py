'''
Lab 25 - Count Words
'''

file = open('alices_adventures_in_wonderland.txt', 'r')  # open input file

punct = '''!()-[]{};:'’’"\,<>./?@#$%^&*_~'''  # string of punctuation symbols

word_set = {}  # dictionary for words

# for each word in the input file, first replace each punctuation character with nothing. Then if the word is not in
# the dictionary of words, add it with a value of one. If the word is in the dictionary, iterate value by one.
for word in file.read().split():
    no_punct = ""
    for char in word:
        if char not in punct:
            no_punct = no_punct + char
    word = no_punct.lower()

    if word not in word_set:
        word_set[word] = 1
    else:
        word_set[word] += 1

# Print the most frequent top 10 out with their counts.
words = list(word_set.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
