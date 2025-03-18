# defining the function
def calculate_interest(principal, rate, time):
    return (principal*rate*time)/100


# getting user input
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate: "))
time = int(input("Enter the time in years: "))

interest = calculate_interest(principal, rate, time)

# printing the results
print(
    f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
