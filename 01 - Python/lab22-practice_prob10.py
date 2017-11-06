'''
Lab 22 - Practice Problems
Problem 10: Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
'''


# CatDog function - Create a 'cat' occurrence counter and 'dog occurrence counter. Loop over the string, counting
# occurrences of cat. Then loop over string again counting occurrences of dog. If cat count and dog count match,
# return true, otherwise return false.
def cat_dog(cats_dogs):
    cat_count = 0
    dog_count = 0
    for i in range(len(cats_dogs)):
        if cats_dogs[i:i + 3] == 'cat':
            cat_count += 1
    for i in range(len(cats_dogs)):
        if cats_dogs[i:i + 3] == 'dog':
            dog_count += 1
    if cat_count == dog_count:
        return True
    else:
        return False


# Prompt for alternating 'cat' and 'dog'.
input_cd = input("Type 'catdogcatdog...': ")

# Pass input string to function and print result
print(cat_dog(input_cd))
