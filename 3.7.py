# array for time of day
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# variable to hold the sum
total_sum = 0

# multi-level list storing the time slot with the heart rate
heart_rate = [[time_slot, int(input(
    f"Enter your heart rate (in BPM) for the {time_slot}: "))]for time_slot in time_slots]

# printing the heart rate at each time of day and calculating the sum
for time_of_day, value in heart_rate:
    print(f"During the {time_of_day}, your heart rate was {value}.")
    total_sum += value

# printing the average
print(f"Average heart rate today: {total_sum/len(time_slots):.2f}")
