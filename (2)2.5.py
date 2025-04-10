def main():
    symbols = "!@#$%&*"
    has_length = has_upper = has_lower = has_numeric = has_symbol = False

    try:
        while not (has_length and has_upper and has_lower and has_numeric and has_symbol):
            has_length = has_upper = has_lower = has_numeric = has_symbol = False
            password = input("Please enter a password: ")

            # ensures the password is between 8 to 20 characters
            if len(password) < 8:
                print("Your password is too short!")
            elif len(password) > 20:
                print("Your password is too long!")
            else:
                has_length = True

            for char in password:
                # ensures there is at least one uppercase letter
                if (char.isupper()):
                    has_upper = True

                # ensures there is at least one lowercase letter
                if (char.islower()):
                    has_lower = True

                # ensures there is at least one number
                if char.isnumeric():
                    has_numeric = True

                # ensures there is a symbol
                if char in symbols:
                    has_symbol = True

        second_password = input("Please enter you password again to confirm: ")

        while password != second_password:
            print("Your reentered password did not match the original")
            second_password = input(
                "Please enter you password again to confirm: ")

        print("Success")

    except:
        print("An error occurred!")


main()
