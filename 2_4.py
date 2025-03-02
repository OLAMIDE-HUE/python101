# 1 kilogram = 2.20462 pounds
conversion_factor = 2.20462

# kilogram sample values
kilogram_1 = 28.4
kilogram_2 = 82.4
kilogram_3 = 63.9
kilogram_4 = 39.8

# pounds sample values
pound_1 = kilogram_1 * conversion_factor
pound_2 = kilogram_2 * conversion_factor
pound_3 = kilogram_3 * conversion_factor
pound_4 = kilogram_4 * conversion_factor

# output statements
print(f"{kilogram_1} kilograms is equivalent to {pound_1:.2f} pounds.")
print(f"{kilogram_2} kilograms is equivalent to {pound_2:.2f} pounds.")
print(f"{kilogram_3} kilograms is equivalent to {pound_3:.2f} pounds.")
print(f"{kilogram_4} kilograms is equivalent to {pound_4:.2f} pounds.")