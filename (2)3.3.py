# defining a pet class
class Pet:
    # class variable
    vet_name = 'Caring Claws Vet'

    # constructor
    def __init__(self, owner_first_name="", owner_last_name="", pet_id=0, pet_name="", pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # getter methods
    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

    # setter methods
    def set_owner_first_name(self, first_name):
        self.__owner_first_name = first_name

    def set_owner_last_name(self, last_name):
        self.__owner_last_name = last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # method displays detail of pet and owner
    def display_pet_info(self):
        print("Vet Name:", self.vet_name)
        print("Owner's First Name:", self.__owner_first_name)
        print("Owner's Last Name:", self.__owner_last_name)
        print("Pet's ID:", self.__pet_id)
        print("Pet's Name:", self.__pet_name)
        print("Pet's Type:", self.__pet_type)


# function checks if a property exists in an object
def check_property(obj, prop):
    return hasattr(obj, prop)


# defining the main function
def main():
    # initializing the first and second objects with constructor
    pet1 = Pet("Conor", "Graham", 145, "Max", "Bird")
    pet2 = Pet("Isabel", "Finley", 163, "Luna", "Cat")

    # initializing third object and assigning variable through setter method
    pet3 = Pet()
    pet3.set_owner_first_name("Carlos")
    pet3.set_owner_last_name("Rosales")
    pet3.set_pet_id(345)
    pet3.set_pet_name("Coco")

    # displaying each objects information
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    # checking for different attributes
    print(check_property(pet1, "_Pet__pet_id"))
    print(check_property(pet2, "_Pet__pet_name"))
    print(check_property(pet3, "vet_name"))


# calling the main function
main()
