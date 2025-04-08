def main():
    # gets the users character
    user_input = input("Enter a character: ")

    # makes sure the user entered only one character
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # converts the character to it's ascii code
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")


main()
