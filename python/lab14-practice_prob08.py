'''
Lab 14 - Practice Problems
Problem 8: Write a function that returns the reverse of a list.
'''


def reverse(nums):  #define reverse funcion
    rev_nums = []  # define reverse list
    for num in nums:  # start for loop
        rev_nums.insert(0, num)  # use insert method to insert each number in sequence into the 0 position of reversed list
    return rev_nums  # output reversed list


values = [1, 12, 2, 53, 23, 6, 17]  # list of values

print(reverse(values))  # pass list to function and print result
