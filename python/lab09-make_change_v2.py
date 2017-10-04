'''
Lab 09 - Make Change
Convert from dollar amount
'''

total = float(input("How much cash do you have? $"))  # prompt for dollar amount as float
total = int(total * 100)  # multiply dollar amount by 100 and convert to int

quarters = total // 25  # find number of quarters
total = total - (quarters * 25)  # subtract value of quarters from total

print(str(quarters), " quarters\n")  # output number of quarters

dimes = total // 10  # find number of dimes
total = total - (dimes * 10)  # subtract value of dimes from total

print(str(dimes), " dimes\n")  # output number of dimes

nickels = total // 5  # find number of nickels
total = total - (nickels * 5)  # subtract value of nickels from total

print(str(nickels), " nickels\n")  # output number of nickels

pennies = total  # find number of pennies

print(str(pennies), " pennies\n")  # output number of pennies
