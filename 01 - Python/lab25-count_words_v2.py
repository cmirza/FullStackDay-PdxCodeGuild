'''
Lab 25 - Count Words
Count how often each unique pair of words is used
'''

# Open text file to read, set to contents. For each char in contents remove punctuation. Then lowercase all chars and
# split at whitespace
with open('alices_adventures_in_wonderland.txt', 'r') as f:
    contents = f.read()
    for char in ''',./\;\"{}[]&@!#$%^*()'?&-''':
        contents = contents.replace(char, '')
    contents = contents.lower()
    contents = contents.split()
    f.close()

pair_set = {}  # define dictionary for word pairs

# for each word in the input file, set word as the current word in the contents and the next word in the contents. If
# the word is not in the dictionary of word pairs, add it with a value of one. If the word is in the dictionary,
# iterate value by one.
for i in range(len(contents) - 1):
    word = contents[i] + " " + contents[i + 1]
    if word in pair_set:
        pair_set[word] = 1
    else:
        pair_set[word] += 1

# Print the most frequent top 10 out with their counts.
words = list(pair_set.items())  # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
