'''
Lab 22 - Practice Problems
Problem 12: Write a function combine_all that takes a list of lists,
and returns a list containing each element from each of the lists.
'''


# CombineAll function - Define combined list. Iterate over the lists in input list, then iterate over the numbers
# within that list. Append number within combined list. Then return combined list.
def combine_all(num_list):
    combined_list = []
    for n_list in num_list:
        for i in n_list:
            combined_list.append(i)
    return combined_list


# List of lists of numbers
nums = [[5, 2, 3], [4, 5, 1], [7, 6, 3]]

# Pass input list to function and print result
print(combine_all(nums))
