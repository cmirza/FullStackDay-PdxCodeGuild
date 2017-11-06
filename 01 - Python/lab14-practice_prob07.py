'''
Lab 14 - Practice Problems
Problem 7: Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
'''


def minimum(nums):  # define function
    min_value = 0  # smallest number in list so far
    for n in nums:  # start loop
        if n < min_value:  # if selected number in list is smaller than smallest number in list so far set it as smallest number
            min_value = n
    return n  # return the smallest number in list


def maximum(nums):  # define function
    max_value = 0  # largest number in list so far
    for n in nums:  # start loop
        if n > max_value:  # if selected number in list is greater than largest number in list so far set it as largest number
            max_value = n
    return n  # return the largest number in list


def mean(nums):  # define function
    sum = 0  # sum of number in list
    for n in nums:  # start loop
        sum = sum + n  # add up numbers in list
    return sum/len(nums)  # divide sum of list by number of items in list and return number


values = [1, 12, 2, 53, 23, 6, 17]  # list values

print("Largest number in list: ", minimum(values), "\n")  # output largest number in list
print("Smallest number in list: ", maximum(values), "\n")  # output smallest number in list
print("Mean of numbers in list: ", mean(values), "\n")  # output the mean of all values in list
