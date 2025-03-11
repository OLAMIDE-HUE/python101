# creates an empty lists to store the user names
names = []

# asks the user for 5 names and appends to names array
for i in range(5):
    names.append(input("Please enter a name: "))


names = [name.lower() for name in names]

# using bubble sort algorithm to sort the names in the array
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True
print(f"Sorted Names: {names}")

# reversing the sorted list
names.reverse()
print(f"Reversed Names: {names}")
