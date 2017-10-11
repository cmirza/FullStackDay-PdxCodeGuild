'''
Lab 20 - Credit Card Validation
'''


# define ccv function
def ccv(num):
    # convert string into list of ints
    num = list(num)
    for i in range(len(num)):
        num[i] = int(num[i])
    # delete check digit
    chk_digit = num[-1]
    del num[-1]
    # reverse list
    rev_nums = []
    for i in num:
        rev_nums.insert(0, i)
    num = rev_nums
    # double every number in list
    for i in range(0, len(num), 2):
        num[i] = num[i]*2
    # subtract 9 for values greater than 9
    for i in range(len(num)):
        if num[i] > 9:
            num[i] = num[i]-9
    # sum elements of the list
    sum = 0
    for i in num:
        sum += num[i-1]
    # compare second digit of sum to check digit and return result
    if chk_digit == (sum % 10):
        return "Valid Credit Card Number."
    else:
        return"Invalid Credit Card Number."


# prompt for input, check number length and pass to function
number = input('Enter a Credit Card Number: ')
if len(number) != 16:
    print("Invalid Credit Card Number.")
else:
    print(ccv(number))
