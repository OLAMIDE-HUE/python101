# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:  # this block runs if the user does not enter an integer
        print("You did not enter in an integer!")


# calling the function
square_number()
