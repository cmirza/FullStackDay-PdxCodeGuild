'''
Lab 11 - Average Numbers
Allow user to create list of numbers
'''

nums = []  # define list

sum = 0  # define sum variable

while True:  # begin input loop
    user_num = input("Enter an integer or type 'done': ")  # prompt for input
    if user_num == "done":  # if user inputs 'done' break loop
        break
    nums.append(int(user_num))  # add input to list as an integer

for i in range(len(nums)):  # tally numbers in list nums
    sum += nums[i]

avg = sum / len(nums)  # divide the sum by number number of elements in list

print("Average: " + str(avg))  # output average
