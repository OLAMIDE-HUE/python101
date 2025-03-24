# defining the main function
def main():
    # dictionary of NATO phonetic words
    nato_alphabet = {'A': "Alpha", 'B': "Bravo", 'C': "Charlie", 'D': "Delta", 'E': "Echo", 'F': "Foxtrot", 'G': "Golf", 'H': "Hotel", 'I': "India", 'J': "Juliett", 'K': "Kilo", 'L': "Lima", 'M': "Mike", 'N': "November", 'O': "Oscar",
                     'P': "Papa", 'Q': "Quebec", 'R': "Romeo", 'S': "Sierra", 'T': "Tango", 'U': "Uniform", 'V': "Victor", 'W': "Whiskey", 'X': "X-ray", 'Y': "Yankee", 'Z': "Zulu"}

    # printing the NATO code for the users word
    for c in word:
        print(nato_alphabet[c])


# get user input
word = input("Please enter a word: ").upper()

# calling the main function
main()
