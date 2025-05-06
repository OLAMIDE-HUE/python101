# function that prints the main menu and options
def main_menu():
    print("Menu:")
    while True:
        try:
            print(
                "Welcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(
                input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")


# checks if the the file exists
def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()  # an array holding each line as an element
        file.close()
        return lines  # returns an array of strings of all the lines in the file
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

# creates a new entry


def create():
    customer = check()
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)  # appends the new entry to the end of the file
    save(customer)

# saves the new changes to the file by writing into it


def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.\n")

# prints out the information of the person with the last name entered


def read():
    customer = check()
    last_name = input(
        "Please enter the last name of the person you are looking for: ").lower()

    for entry in customer:
        if last_name in entry.lower().split(", ")[1]:
            print(f"Information on {last_name}: ", entry)
            return
    print("Person Not found!")

# makes changes to an existing entry


def update():
    customer = check()
    last_name = input(
        "Please enter the last name of the person you are looking for: ").lower()
    counter = 0

    # updates the entry with the last name
    for entry in customer:
        if last_name in entry.lower().split(", ")[1]:
            fname = input("Please enter the new customer\'s first name: ")
            lname = input("Please enter the new customer\'s last name: ")
            phone = input("Please enter the new customer\'s phone: ")
            email = input("Please enter the new customer\'s email: ")
            person = f"{fname}, {lname}, {phone}, {email}\n"
            customer[counter] = person
            save(customer)
            return
        counter += 1

# deletes an existing entry


def delete():
    customer = check()
    last_name = input(
        "Please enter the last name of the person you are looking for: ").lower()
    counter = 0

    # deletes the entry with the last name
    for entry in customer:
        if last_name in entry.lower().split(", ")[1]:
            del customer[counter]
            save(customer)
            return
        counter += 1

# main function runs a function depending on the option chosen


def main():
    choice = 0
    while choice != 5:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
    print("\nData saved as customer_list.txt\n")


# calling main function
main()
