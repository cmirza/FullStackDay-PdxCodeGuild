'''
Lab 24 - Bogo Sort
'''


import random
import time


# Function to generate a random number between 0-100 and append it to a list for the length requested.
def random_list(n):
    generated_list = []
    for i in range(n):
        generated_list.append(random.randint(0, 100))
    return generated_list


# Function to shuffle, starting at the first element of the list and swapping one by one.
def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
    return nums


# Function to check if list is sorted, if current number is greater than next number, returns false. Otherwise if
# current number is less than or equal to next number, passes until it returns true.
def is_sorted(nums):
    for i in range(len(nums[:-1])):
        if nums[i] > nums[i+1]:
            return False
        elif nums[i] <= nums[i+1]:
            pass
    return True


# Function for bogosort, runs a loop randomly sorting the list, if random sort does not pass is_sorted, loop
# continues. Otherwise if the random sort passes is_sorted, loop is broken and time elapsed is printed.
def bogosort(nums):
    while True:
        for i in range(len(nums)):
            j = random.randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        if is_sorted(nums) is False:
            pass
        elif is_sorted(nums) is True:
            return "Sorted in " + str(time.process_time()) + " seconds."


# passes input of how long a list to sort to random_list, then passes that output to shuffle and passes that output to
# bogosort and prints result.
print(bogosort(shuffle(random_list(int(input("How long of a list do you want to sort? "))))))
