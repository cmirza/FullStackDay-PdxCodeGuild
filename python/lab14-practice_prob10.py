'''
Lab 14 - Practice Problems
Problem 10: Write a function to move all the elements of a list with value less than 10 to a new list and return it.
'''


def extract_less_than_ten(nums):  # define function
    lessthan10 = []  # define list for elements less than 10
    for num in nums:  # run through elements in list
        if num < 10:  # if element is less than 10, add it to list
            lessthan10.append(num)
    return lessthan10  # output list of list of elements less than 10


values = [1, 12, 2, 53, 23, 6, 17]  # list of values


print(extract_less_than_ten(values))  # pass list to function and print result
