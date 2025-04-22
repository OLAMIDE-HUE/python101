# defining employee superclass
class Employee:

    # superclass constructor
    def __init__(self, employee_name="", employee_number=0):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # getter methods
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    # setter methods
    def set_employee_name(self, name):
        self.__employee_name = name

    def set_employee_number(self, num):
        self.__employee_number = num

# defining ProductionWorker subclass


class ProductionWorker(Employee):

    # subclass constructor
    def __init__(self, employee_name="", employee_number=0, shift_number=0, hourly_pay_rate=0):
        super().__init__(employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # getter methods
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_pay_rate

    # setter methods
    def set_shift_number(self, num):
        self.__shift_number = num

    def set_hourly_rate(self, rate):
        self.__hourly_pay_rate = rate


# defining an exception class for an invalid shift number
class InvalidShiftNum(Exception):
    pass

# defining the main function


def main():
    try:
        # creating an instance of production worker
        p_worker = ProductionWorker()

        print("""Enter the following details of the Employee
    --------------------------------------------""")

        # storing employee details
        p_worker.set_employee_name(input("Enter Employee Name: "))
        p_worker.set_employee_number(int(input("Enter Employee Number: ")))
        p_worker.set_shift_number(
            int(input("Enter Shift Number(\"1\" for day, \"2\" for night): ")))
        if (p_worker.get_shift_number() != 1 and p_worker.get_shift_number() != 2):
            raise InvalidShiftNum(
                "ERROR!!!!! You did not enter \"1\" or \"2\" for your shift number!")

        p_worker.set_hourly_rate(float(input("Enter Pay Rate: ")))

        print("""-------------------------------------------------------
    Details of Employee:
    -------------------------------------------------------""")

        # converts 1 to Day and 2 to night
        if (p_worker.get_shift_number() == 1):
            shift = "Day"
        else:
            shift = "Night"

        print("Name:", p_worker.get_employee_name())
        print("Employee Number:", p_worker.get_employee_number())
        print("Shift:", p_worker.get_shift_number())
        print("Pay Rate:", p_worker.get_hourly_rate())

    # exception runs if the user does not enter a number when appropriate
    except ValueError:
        print("You did not enter a number!\nPlease try again!")

    except InvalidShiftNum as i:
        print(i)
    # handles any other exception that might come up
    except:
        print("ERROR!!!\nSomething went Wrong!")


# calling the main function
main()
