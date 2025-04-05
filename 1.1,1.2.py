from random import randrange

# defining the function


def main():

    # generates a random number between 1 and 100 inclusively
    number = randrange(1, 101)

    # gets the users guess
    print("Guess a number between 1 and 100")
    users_guess = int(input("Please enter in your guess: "))

    # prompts the user to keep guessing a number till its right
    while (users_guess != number):

        # gets the absolute difference between the users guess and actual number
        diff = abs(number - users_guess)

        # tells the user how close they are to the actual number
        if diff <= 5:
            print("Very Hot")
        elif diff <= 15:
            print("Hot")
        elif diff <= 25:
            print("Cool")
        else:
            print("Cold")

        # prompts the user to guess again
        users_guess = int(input("Please enter in your guess: "))

    # tells the user they guessed right
    print("Congratulations you guessed right!!!")


# calling the function
main()
