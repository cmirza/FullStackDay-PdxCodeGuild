'''
Using lists with .split() function
'''

adjective1 = input("Give me an adjective:\n")
input_noun = input("Give me two nouns separated by commas:\n")
input_noun.split(", ")
noun1, noun3 = input_noun.split(", ")
noun2 = input("Give me a plural noun:\n")
verb1 = input("Give me a verb ending in 'ed':\n")
print(" There was a " + adjective1 + " woman who lived in a " + noun1 + ".\n She had so many " + noun2 + " she didnt know what to do.\n She gave them some broth without any " + noun3 + ".\n She " + verb1 + " them all soundly and put them to bed.\n")
