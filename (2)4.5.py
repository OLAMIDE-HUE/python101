# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week

from datetime import datetime

# defining the main function


def main():

    print("\n\n")
    try:

        # gets todays date and time
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(
            input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))

        # calculates the users birthday
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")

        # formatting to remove time
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        # calculating age in days
        delta = today - birthday
        print(f'Difference is {delta.days} days')

        # calculating age in weeks
        delta_weeks = delta.days // 7
        print(f'Your age in weeks is: {delta_weeks}')

        # calculating age in months
        delta_months = delta.days // 30.41
        print(f'Your age in months is: {delta_months}')

        # calculating age in years
        delta_years = delta.days // 365.2425
        print(f'You are {delta_years} years old', end=' ')

        # calculating the remainder of the months after the years
        delta_remaining_months = (delta.days % 365.2425) // 30.41
        print(f'and {delta_remaining_months} months')

        # calculating age in hours
        delta_hours = delta.days * 24
        print(f'Your age in hours is: {delta_hours}')

        # calculating age in minutes
        delta_minutes = delta.days * 24 * 60
        print(f'Your age in minutes is: {delta_minutes}')

        # calculating age in seconds
        delta_seconds = delta.days * 24 * 3600
        print(f'Your age in seconds is: {delta_seconds}')

    except Exception as e:
        print(f"ooooops!!!:  {e}")
        main()


main()
