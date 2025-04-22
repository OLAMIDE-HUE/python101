# generator function to output the cartesian product of a list
def two_letter_combinations(l_character):
    for i in l_character:
        for j in l_character:
            # yields the combination of the letters
            yield i + j

# defining main function


def main():
    # 5-letter list
    my_list = ['a', 'b', 'c', 'd', 'e']

    # prints all combinations form the generator function
    for i in two_letter_combinations(my_list):
        print(i)


# calling main function
main()
