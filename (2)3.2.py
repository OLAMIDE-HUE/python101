# defining the Person class
class Person:

    # Person's constructor
    def __init__(self, name="", address="", age=-1, phone_number=0):
        # private variables
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # getter methods
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getPhoneNumber(self):
        return self.__phone_number

    # setter methods
    def setName(self, n):
        self.__name = n

    def setAddress(self, ad):
        self.__address = ad

    def setAge(self, a):
        self.__age = a

    def setPhoneNumber(self, p):
        self.__phone_number = p


# initializing first and second Person objects with the constructor
person1 = Person("John", "123 Main Street", 17, 3892349298)
person2 = Person("Mark", "321 New Street", 23, 9829834723)

# initializing the third Person object with the setter method
person3 = Person()

person3.setName("Hunter")
person3.setAddress("213 Previous Street")
person3.setAge(10)
person3.setPhoneNumber(1297836576)


# printing out the information from each object
print(f"""Name: {person1.getName()} 
Address: {person1.getAddress()}
Age: {person1.getAge()}
Phone Number: {person1.getPhoneNumber()}""")

print(f"""Name: {person2.getName()} 
Address: {person2.getAddress()}
Age: {person2.getAge()}
Phone Number: {person2.getPhoneNumber()}""")

print(f"""Name: {person3.getName()} 
Address: {person3.getAddress()}
Age: {person3.getAge()}
Phone Number: {person3.getPhoneNumber()}""")
