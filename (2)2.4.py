def main():
    book_titles = []

    # user enters 10 books
    while (len(book_titles) != 10):

        # appends each book title to the end of the list and capitalizes the first letter
        book_titles.append(input("Please enter a book title: ").title())

    # sorting the array
    books_sorted = sorted(book_titles)

    # printing each book title
    for book in books_sorted:
        print(book)


# calling the function
main()
