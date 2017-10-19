'''
Lab 22 - Practice Problems
Problem 13: Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
'''


# Fibonacci function - Define list for Fibonacci numbers. 'a, b' are the initial numbers for calculating. Run loop for
# range of amount of numbers wanted, minus one. a equals b and b is the sum of a plus b. Append a to Fibonacci list.
# Then return Fibonacci list.
def fibonacci(length):
    f_list = []
    a, b = 0, 1
    for i in range(length-1):
        a, b = b, a + b
        f_list.append(a)
    return f_list


# prompt for length of Fibonacci sequence wanted
input_num = int(input("How long of a Fibonacci sequence do you want: "))

# Pass input number to function and print result
print(fibonacci(input_num))
