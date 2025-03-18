# defining global variables
global pounds_to_kilograms
pounds_to_kilograms = 0.453592
global inches_to_meter
inches_to_meter = 0.0254

# defining the BMI_conversion function
def BMI_conversion(weight, height):
    bmi = weight / (height * height)
    return bmi

# getting the user inputs
weight_in_pounds = int(input("Enter your weight in pounds: "))
height_in_inches = int(input("Enter your height in inches: "))

# converting pounds and inches to kilograms and meters
weight_in_kilograms = weight_in_pounds * pounds_to_kilograms
height_in_meters = height_in_inches * inches_to_meter

# storing the BMI value to result
result = BMI_conversion(weight_in_kilograms, height_in_meters)

# printing the users BMI
print(f"Your BMI is {result:.2f}")

# determining what category the user is in
if (result < 18.5):
    print("You are in the underweight category")
elif (result >= 18.5 and result < 25):
    print("You are in the normal weight category")
elif (result >= 25 and result < 30):
    print("You are in the overweight category")
elif (result >= 30):
    print("You are in the obese category")
