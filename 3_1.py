# gets the users age
age = int(input("What is your age?: "))

# checks if the user is old enough to drive
if (age >= 16):
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")

# checks if the user is old enough to vote
if (age >= 18):
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
    
# checks if the user can buy alcohol legally
if (age >= 21):
    print("You can buy alcohol legally")
else:
    print("You cannot buy alcohol legally")

# checks if the user can get a senior discount
if (age >= 65):
    print("You are eligible for a senior discount")
else:
    print("You are not eligible for a senior discount")