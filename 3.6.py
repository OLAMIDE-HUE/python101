# a list of to seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# printing the available seats
print(f"These are the available seats:", end=" ")
for seat in seats:
    print(seat, end=",")

while len(seats) != 0:
    seatNum = int(input(
        "Please enter a seat , 1-20,you would like to purchase or enter \"0\" to end the purchase process: "))
    if seatNum < 0 or seatNum > 20:
        print("Please enter in a number from 1-20!")
        continue
    if (seatNum == 0):
        break
    if seatNum in seats:
        for i in range(len(seats)):
            if seatNum == seats[i]:
                del seats[i]
                break
    else:
        print(f"Seat {seatNum} has already been purchased! Please try again!")

print(f"Remaining available seats are {seats}")
print("This is the end of the program!")
