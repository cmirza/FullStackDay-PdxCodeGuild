'''
Lab 11 - Average Numbers
'''

nums = [5, 0, 8, 3, 4, 1, 6]  # list of numbers

sum = 0  # define sum variable

for i in range(len(nums)):  # tally numbers in list nums
    sum=sum+nums[i]

avg = sum / len(nums)  # divide the sum by number number of elements in list

print("Average: " + str(avg))  # output average
