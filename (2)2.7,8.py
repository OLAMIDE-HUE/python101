def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    try:

        # gets the user's index
        users_index = int(
            input("Please enter what index you would like to replace: "))

        # gets the user's new artist
        users_artist = input("Please enter a new artists name: ")

        # replaces the chosen index with the new artist
        top_artists[users_index] = users_artist

        # prints the new array
        print(top_artists)

    # runs if the user does not enter an integer for the index or enters an invalid index
    except (ValueError, IndexError):
        print("An input error occurred.")
    except:
        print("There is an error!!!")


# calling the main function
main()
