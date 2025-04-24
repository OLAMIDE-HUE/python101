# defining the main function
def main():
    try:

        # counts how many lines are in the file
        line_counter = 0

        # gets the total value of the file
        total_num = 0.0

        # opening the file directory
        f = open("C:\\Users\\olami\\OneDrive\\Desktop\\Python Repository\\python101\\(2)4.3\\sales_totals.txt", 'rt')

        # reading the first line
        line = f.readline()

        # runs when line is not at the end of the file
        while line != '':

            # incrementing the line_counter
            line_counter += 1

            # converts the line to a float and strips the newline character
            num = float(line.strip())

            # converting the line being read to a float
            total_num += num

            # printing the current line and adds commas to the number
            print(f"{num:,.2f}")

            # reading the next line
            line = f.readline()

        # closing the file
        f.close()

        # printing the total and number of lines
        print("Total:", f"{total_num:,.2f}")
        print("Number of entries:", line_counter)

        # calculates the average of the file
        print("Average:", f'{total_num/line_counter:,.2f}')

    except ValueError:
        print("ERROR: There is a value in the file that is not a number.")
    except IOError:
        print("ERROR: Could not open the file.")


# calling the main function
main()
