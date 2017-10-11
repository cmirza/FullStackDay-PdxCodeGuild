'''
Lab 22 - Practice Problems
Problem 2: Print out every other element of a list, first using a while loop, then using a for loop.
'''


def print_every_other_while(num):  # define while loop function
    new_num = []  # define new number list
    i = 0  # define iterator
    while i in range(len(num)):  # while iterator is in range of the length of number list
        new_num.append(num[i])  # append number to new number list
        i += 2  # iterate by two
    print(new_num)  # print new list


def print_every_other_for(num):  # define for loop function
    new_num = []  # define new number list
    for i in range(0, len(num), 2):  # run loop from 0, for length of number list, incrementing by two
        new_num.append(num[i])  # append number to new number list
    print(new_num)  # print new list


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # number list

print_every_other_for(nums)  # pass list to function
print_every_other_while(nums)  # pass list to function
