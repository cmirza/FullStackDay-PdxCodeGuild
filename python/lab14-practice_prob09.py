'''
Lab 14 - Practice Problems
Problem 9: Write a function to find all common elements between two lists.
'''


def common_elements(nums1, nums2):  # define function
    matches = []  # define list for matched elements
    for num in nums1:  # run through elements in first list
        if num in nums2:  # if current element matches element in second list, append it to list of matched elements
            matches.append(num)
    print(matches)  # output matched elements


values1 = [1, 12, 2, 53, 23, 6, 17]  # first list of values

values2 = [9, 25, 12, 17, 78, 4, 6]  # second list of values

common_elements(values1, values2)  # pass both lists to function
