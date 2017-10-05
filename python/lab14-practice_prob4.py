'''
Lab 14 - Practice Problems
Problem 4: Write a function using random.randint and subscription to get a random element of a list and return it.
'''


def random_element(x):  # define function
    import random  # import random module
    chosen_name = x[random.randint(0, (len(x)-1))]  # randomly choose one of the items in the list
    return chosen_name  # output item


fruits = ['apples', 'bananas', 'pears', 'cherries']  # declare list

print(random_element(fruits))  # pass list to the function and print its output
