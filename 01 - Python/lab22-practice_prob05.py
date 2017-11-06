'''
Lab 22 - Practice Problems
Problem 5: Write a function that merges two lists into a single list, where each element of the
outlist list is another list containing two elements.
'''


def merge_list(lst1, lst2):  # define merge list function
    merged_lst = []  # define merged list
    len_lst = min(len(lst1), len(lst2))  # set length of list to the smaller list
    for i in range(len_lst):  # loop through both lists and append corresponding elements to merged list
        merged_lst.append([lst1[i], lst2[i]])
    return merged_lst  # return merged list


list_1 = [5, 2, 1]  # define list
list_2 = [6, 8, 2]  # define list

print(merge_list(list_1, list_2))  # pass lists to function and print result
