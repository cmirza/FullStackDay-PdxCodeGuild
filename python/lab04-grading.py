input_grade = input("What percentage did you get:")
grade = int(input_grade)

if grade > 100:
    print("I don't think so...\n")
elif grade >= 90:
        print("You've got an A!\n")
elif grade >= 80:
        print("You've got an B!\n")
elif grade >= 70:
        print("You've got an C!\n")
elif grade >= 60:
        print("You've got an D!\n")
elif grade >= 0:
        print("You've got an F!\n")
elif grade < 0:
        print("I don't think so...\n")