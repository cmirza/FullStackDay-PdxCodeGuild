'''
Lab 03 - Mad Libs
Using lists with .split() function
'''

adjective1 = input("Give me an adjective:\n") # prompt for adjective
input_noun = input("Give me two nouns separated by commas:\n") # prompt for two nouns separated by comma
input_noun.split(", ") # define comma as split point
noun1, noun3 = input_noun.split(", ") # use split function on the string
noun2 = input("Give me a plural noun:\n") # prompt for noun
verb1 = input("Give me a verb ending in 'ed':\n") # prompt for verb

print(" There was a " + adjective1 + " woman who lived in a " + noun1 + ".\n She had so many " + noun2 + " she didnt know what to do.\n She gave them some broth without any " + noun3 + ".\n She " + verb1 + " them all soundly and put them to bed.\n") # print story
