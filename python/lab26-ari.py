'''
Lab 26 - Compute Automated Readability Index
'''

import math

# Open text file to read, set to contents, lowercase all chars, remove all punctuation chars, replace !? with periods
with open('alices_adventures_in_wonderland.txt', 'r') as f:
    contents = f.read()
    contents = contents.lower()
    for char in "\n":  # replace new line with space
        contents = contents.replace(char, ' ')
    for char in ''',/\;:\"{}[]&@#$%^*()’‘'&-''':  # remove punctuation chars
        contents = contents.replace(char, '')
    for char in '!?':
        contents = contents.replace(char, '.')

# loop through characters in string and count for every alpha or numerical char
ari_chars = 0
characters = 'abcdefghijklmnoqrstuvwxyz1234567890'
for char in contents:
    if char in characters:
        ari_chars += 1

# split words on whitespace in contents, get length of list for word count
words = contents.split()
ari_words = len(words)

# split sentences on periods in contents, get length of list for sentences count
sentences = contents.split('.')
ari_sentences = len(sentences)

# print character, word and sentence count
print('Characters:\t', ari_chars)
print('Words:\t\t', ari_words)
print('Sentences:\t', ari_sentences)

# dictionary for ARI scale
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# calculate ARI score
ARI = int(math.ceil(4.71 * (ari_chars / ari_words) + 0.5 * (ari_words / ari_sentences) - 21.43))

# print output
print(' --------------------------------------------------------\n', 'The ARI for', f.name, 'is', ARI, '\n This corresponds to a', ari_scale[ARI]['grade_level'], 'of difficulty', '\n that is suitable for an average person', ari_scale[ARI]['ages'], 'years old.\n', '--------------------------------------------------------')
