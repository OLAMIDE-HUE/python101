# gets two integers from the user
value1 = int(input("Enter an integer: "))
value2 = int(input("Enter a different integer: "))

# checks if the user entered in two distinct numbers
if (value1 == value2):
    print("The two numbers are the same! Please enter two distinct numbers!")
else:
    # checks if both numbers are positive (using and)
    if (value1 > 0 and value2 > 0):
        print("Both numbers are positive: True")
    else:
        print("Both numbers are positive: False")

    # checks if both numbers are negative (using and)
    if (value1 < 0 and value2 < 0):
        print("Both numbers are negative: True")
    else:
        print("Both numbers are negative: False")

    # checks if one of the numbers are even (using or)
    if ((value1 % 2) == 0 or (value2 % 2) == 0):
        print("At least one number is even: True")
    else:
        print("At least one number is even: False")

    # checks if one of the numbers is divisible by 4 (using or)
    if ((value1 % 4) == 0 or (value2 % 4) == 0):
        print("At least one of the numbers is divisible by 4: True")
    else:
        print("At least one of the numbers is divisible by 4: False")

    # checks if the first number is odd (using not)
    if (not ((value1 % 2) == 0)):
        print("The first number is odd: True")
    else:
        print("The first number is odd: False")

    # checks if the second number is zero
    if (not (value2 == 0)):
        print("The second number is zero: False")
    else:
        print("The second number is zero: True")
