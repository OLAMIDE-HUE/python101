# list containing all the days of the week
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

# list that will store steps taken on each day
steps = []

# track total steps taken
total = 0

# ask user how many steps they took on each day
for i in range(len(days)):
    steps.append(int(input(f"How many steps did you take on {days[i]}? ")))

# prints how many steps was taken on each day and calculates total steps
for i in range(len(days)):
    print(f"On {days[i]}, you took {steps[i]} steps!")
    total += steps[i]

# prints total and average steps
print(f"Total steps: {total}")
print(f"Average steps: {total/len(steps)}")
