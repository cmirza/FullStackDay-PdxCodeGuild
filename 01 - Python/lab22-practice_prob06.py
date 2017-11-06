'''
Lab 22 - Practice Problems
Problem 6: Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
'''


# Opposite function - If both num1 and num2 are greater than or equal to zero, return false. If both num1 and num2 are
# less than 0, return false. Otherwise, return true.
def opposite(num1, num2):
    if num1 >= 0 and num2 >= 0:
        return False
    if num1 < 0 and num2 < 0:
        return False
    else:
        return True


# Prompt for two numbers.
nums1 = int(input("Enter a positive or negative number: "))
nums2 = int(input("Enter a positive or negative number: "))

# Pass numbers to function and print result.
print(opposite(nums1, nums2))
