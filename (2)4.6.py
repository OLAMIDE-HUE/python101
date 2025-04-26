# importing calendar and datetime modules
import calendar
import datetime

# defining main function


def main():
    # current year
    current_year = datetime.datetime.now().year

    try:
        # users birth month represented as a number
        birth_month = int(input(
            "Enter a number between 1 to 12 for your birth month (Ex: '1' for January): "))

        # raises an exception is the birth month is not between 1 and 12
        if birth_month not in range(1, 13):
            raise Exception

        # prints the calendar birth month for this year
        print(calendar.month(current_year, birth_month))
    except ValueError:
        # prints is the user did not enter an integer
        print("ERROR: You did not enter an integer")
        main()
    except Exception:
        # prints when the birth month is not between 1 and 12
        print("ERROR: You did not enter an integer between 1 and 12")
        main()


# calling main function
main()
