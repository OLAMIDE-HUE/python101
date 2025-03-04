# gets the users total budget and bills
total_budget = float(input("Please enter your net monthly income: "))
housing_spending = float(
    input("Please enter the amount you spend on housing: "))
utilities_spending = float(
    input("Please enter the amount you spend on utilities: "))
groceries_spending = float(
    input("Please enter the amount you spend on groceries: "))
transportation_spending = float(
    input("Please enter the amount you spend on transportation: "))
health_care_spending = float(
    input("Please enter the amount you spend on health care: "))
personal_care_spending = float(
    input("Please enter the amount you spend on personal care: "))
clothing_spending = float(
    input("Please enter the amount you spend on clothing: "))
debt_spending = float(input("Please enter the amount you spend on debt: "))

# gets the percentage of each spending category
housing_spending_percentage = (housing_spending/total_budget)*100
utilities_spending_percentage = (utilities_spending/total_budget)*100
groceries_spending_percentage = (groceries_spending/total_budget)*100
transportation_spending_percentage = (transportation_spending/total_budget)*100
health_care_spending_percentage = (health_care_spending/total_budget)*100
personal_care_spending_percentage = (personal_care_spending/total_budget)*100
clothing_spending_percentage = (clothing_spending/total_budget)*100
debt_spending_percentage = (debt_spending/total_budget)*100

# outputs the calculated percentages
print(
    f"Your housing spending is {housing_spending_percentage:.2f}% of your total budget")
print(
    f"Your utilities spending is {utilities_spending_percentage:.2f}% of your total budget")
print(
    f"Your groceries spending is {groceries_spending_percentage:.2f}% of your total budget")
print(
    f"Your transportation spending is {transportation_spending_percentage:.2f}% of your total budget")
print(
    f"Your health care spending is {health_care_spending_percentage:.2f}% of your total budget")
print(
    f"Your personal care spending is {personal_care_spending_percentage:.2f}% of your total budget")
print(
    f"Your clothing spending is {clothing_spending_percentage:.2f}% of your total budget")
print(
    f"Your debt spending is {debt_spending_percentage:.2f}% of your total budget")