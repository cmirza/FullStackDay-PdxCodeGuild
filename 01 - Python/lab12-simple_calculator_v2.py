'''
Lab 12 - Simple Calculator
With while loop
'''

while True:  # begin input loop
    oper = input("What is the operation you'd like to perform? ")  # prompt for operator

    if oper == "done":  # if user inputs 'done' print goodby and break loop
        print("Goodbye!")
        break

    num_1 = input(str("What is the first number? "))  # prompt for the first operand
    num_2 = input(str("What is the second number? "))  # prompt for the second operand

    sum = eval(num_1+oper+num_2)  # evaluate equation

    print(str(num_1) + oper + str(num_2) + "=" + str(sum))  # concatenate operands and operator, evaluate and print.
