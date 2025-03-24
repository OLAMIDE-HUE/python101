# defining the main function
def main():
    # creating a tuple
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials',
                           'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')

    # printing all the classes in the tuple
    for programming_class in programming_classes:
        print(programming_class)

    # printing number of classes in tuple
    print(f"There are {len(programming_classes)} classes in the tuple")


print("The classes in the tuple are:")
main()
