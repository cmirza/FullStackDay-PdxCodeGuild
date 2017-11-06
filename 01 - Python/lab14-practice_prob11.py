'''
Lab 14 - Practice Problems
Problem 11: Write a function to combine two lists of equal length into one, alternating elements.
'''


def combine(list1, list2):  # define combine function
    comb_list = []  #define combinded list
    for i in range(len(list1)):  # start loop with range the length of first loop
        comb_list.append(list1[i])  # append item from first list in iteration position to combined list
        comb_list.append(list2[i])  # append item from second list in iteration position to combined list
    return comb_list  # return combined list


values1 = [1, 2, 3, 4, 5, 6, 7]  # define first list
values2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # define second list

print(combine(values1, values2))  # pass lists to function and print result
