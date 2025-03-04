# variable to hold the initial number of beers
num = 99

# loops through each decrement from 99 till there are no bottles left
while (num != 1):
    print(f"{num} bottles of beer on the wall\n{num} bottles of beer\nTake one down, pass it around")
    print(f"{num-1} bottles of bear on the wall!\n")
    num -= 1
else:
    print(f"{num} bottle of beer on the wall\n{num} bottle of beer\nTake one down, pass it around")
    print("No bottles of bear on the wall!")
