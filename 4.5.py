# defining the factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# getting user input
num = int(input("Please enter a nonnegative number: "))

# ensures the user enters zero or a positive number
while (num < 0):
    num = int(input("Please enter a nonnegative number: "))

# printing factorial of user's number
print(factorial(num))
