# addition operation
def add(a, b):
    return a + b

# subtraction operation


def subtract(a, b):
    return a - b

# multiplication operation


def multiply(a, b):
    return a * b

# division operation


def divide(a, b):
    return a / b


def main():
    try:
        named_operations = ["addition", "subtraction",
                            "multiplication", "division"]

        # gets which operation the user wants to compute
        operation = input("""Please enter which operation you would like to complete.
                          \"Addition\", \"Subtraction\", \"Multiplication\", \"Division\"""")

        # checks if the user enters "Addition", "Subtraction", "Multiplication", "Division"
        while operation.lower() not in named_operations:
            print("You did not enter any of the operations please try again")
            operation = input(
                """Please enter which operation you would like to complete: \"Addition\", \"Subtraction\", \"Multiplication\", \"Division\"""")

        # gets the numbers from the user
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))

        # does the operation the user inputs
        if (operation.lower() == "addition"):
            print("Result: ", add(num1, num2))
        elif (operation.lower() == "subtraction"):
            print("Result: ", subtract(num1, num2))
        elif (operation.lower() == "multiplication"):
            print("Result: ", multiply(num1, num2))
        elif (operation.lower() == "division"):
            print("Result: ", divide(num1, num2))

    # runs if the second number is 0 and the operation is division
    except ZeroDivisionError:
        print("ERROR!!!\nPlease do not divide by zero")

    # runs if the user does not enter a number
    except ValueError:
        print("ERROR!!!\nPlease enter an integer!")

    # runs if there is any other exceptions
    except:
        print("ERROR!!!")


main()
