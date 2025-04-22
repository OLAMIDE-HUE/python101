# subclass of base exception class
class NotNumericError(Exception):

    # constructor
    def __init__(self, num, message):
        super().__init__(message)
        self.number = num

# defining the main function


def main():
    done = False

    while not done:
        try:
            # prompts the user for an input
            num = input("Enter a number: ")

            if not num.isnumeric():
                raise NotNumericError(num, "is not a number")

        except NotNumericError as n:
            print(n.number, n)

        else:
            done = True
            print("You entered a valid number!")

        finally:
            print("This is the end of the program!")


# calling the main function
main()
