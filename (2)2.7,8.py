def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    try:
        users_index = int(
            input("Please enter what index you would like to replace: "))
        users_artist = input("Please enter a new artists name: ")

        top_artists[users_index] = users_artist

        print(top_artists)
    except (ValueError, IndexError):
        print("An input error occurred.")
    except:
        print("There is an error!!!")


main()
