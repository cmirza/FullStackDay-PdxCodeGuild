'''
Lab 14 - Practice Problems
Problem 5: Write a function that returns the maximum of 3 parameters.
'''


def maximum_of_three(x):  # define function
    max_value = 0  # largest number in list so far
    n = 0  # position in list
    for n in x:  # start loop
        if n > max_value:  # if selected number in list is greater than largest number in list so far set it as largest number
            max_value = n
    return n  # return the largest number in list


text_nums = input("Enter three numbers separated by commas: ")  # prompt to enter three numbers
text_nums = text_nums.split(",")  # split input by commas
text_nums = [int(i) for i in text_nums]  # convert str in list to int

print(maximum_of_three(text_nums))  # pass list to function and print result
