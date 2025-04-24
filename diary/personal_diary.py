# defining a main function
def main():

    # gets users input for date
    date = input("Enter the current date (Ex: 11/30/2009): ")

    # gets users input for time
    time = input("Enter the current time (Ex: 19:20): ")

    # gets users input for the diary text
    diary_entry = input("Enter your Diary Entry: ")

    # opening the file with append
    diary = open("C:\\Users\\olami\\OneDrive\\Desktop\\Python Repository\\python101\\diary\\diary.txt", "a")

    # writing the given information in the file
    diary.write(date + " " + time + "\n" + diary_entry + '\n\n')

    # closing the file
    diary.close()


# calling the main function
main()
