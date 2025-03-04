# gets the users numerical grade
grade = int(
    input("Please enter in a numerical grade between 1 and 100 inclusively: "))

# converts numerical grade to letter grade and prints the letter grade
if (grade < 0 or grade > 100):
    print("Please enter in a numerical grade between 1 and 100 inclusively: ")
elif (grade >= 90):
    print(f"The letter grade is: A")
elif (grade >= 80):
    print(f"The letter grade is: B")
elif (grade >= 70):
    print(f"The letter grade is: C")
elif (grade >= 60):
    print(f"The letter grade is: D")
else:
    print(f"The letter grade is: F")
