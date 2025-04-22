# defining Pet class
class Pet:
    def __init__(self, kind='', breed='', name=''):
        self.kind = kind
        self.breed = breed
        self.name = name

    # getter methods

    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # setter methods

    def set_kind(self, kind):
        self.kind = kind

    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name

    # method prints the Pet's details
    def print_details(self):
        print("Pet's Kind:", self.kind)
        print("Pet's Breed:", self.breed)
        print("Pet's Name:", self.name)


# defining the main function
def main():
    # three Pet objects
    pet1 = Pet("Dog", "Bulldog", "Max")
    pet2 = Pet("Cat", "Abyssinian", "Luna")
    pet3 = Pet("Bird", "Finch", "Rex")

    # printing all the details for the objects
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    print("The breed of pet1 is " + getattr(pet1, "breed"))
    print("The class used to instantiate pet2 is ", type(pet2))
    print("The module of pet3 is " + pet3.__module__)


# calling the main function
main()
