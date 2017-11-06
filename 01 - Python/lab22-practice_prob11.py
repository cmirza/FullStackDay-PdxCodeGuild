'''
Lab 22 - Practice Problems
Problem 11: Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
'''


# EvenEven function - Set counter of even numbers. Loop over numbers in list, if number remainder 2 is 0, iterate
# counter. Otherwise continue looping through list. Then check if even number count remainder 2 is 0, if it is return
# true, otherwise return false.
def eveneven(nums):
    evenflow = 0
    for i in nums:
        if i % 2 == 0:
            evenflow += 1
        else:
            continue
    if evenflow % 2 == 0:
        return True
    else:
        return False


# Lists of numbers
num_list_1 = [5, 6, 2]
num_list_2 = [5, 5, 2]

# Pass input lists to function and print result
print(eveneven(num_list_1))
print(eveneven(num_list_2))
