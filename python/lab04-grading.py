'''
Lab 04 - Grading
'''

grade = int(input("What percentage did you get:")) # prompt for percentage

if grade > 100: # if grade is over 100, give an error
    print("I don't think so...\n")
elif grade >= 90: # if grade is greater than or equal to 90, it was an A
        print("You've got an A!\n")
elif grade >= 80: # if grade is greater than or equal to 80, it was an B
        print("You've got an B!\n")
elif grade >= 70: # if grade is greater than or equal to 70, it was an C
        print("You've got an C!\n")
elif grade >= 60: # if grade is greater than or equal to 60, it was an D
        print("You've got an D!\n")
elif grade >= 0: # if grade is greater than or equal to 0, it was an F
        print("You've got an F!\n")
elif grade < 0: # if grade is less than 0, give an error
        print("I don't think so...\n")