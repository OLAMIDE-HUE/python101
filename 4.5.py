# defining the factorial function
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n-1)


# getting user input
num = int(input("Enter a nonnegative number: "))

# printing factorial of user's number
print(factorial(num))
