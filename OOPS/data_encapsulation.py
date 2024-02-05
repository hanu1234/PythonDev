#  Example 1: Private Attributes and Methods

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # private attribute

    def __calculate_area(self):  # private method
        return 3.14 * self.__radius * self.__radius

    def get_area(self):
        return self.__calculate_area()


# Creating an instance of the Circle class
my_circle = Circle(5)

# Accessing the private attribute using name mangling
print("Radius:", my_circle._Circle__radius)

# Accessing the area through a public method
print("Area:", my_circle.get_area())


# Example 2: Using Property for Getter and Setter
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance not updated.")

# Creating an instance of the BankAccount class
account = BankAccount(1000)

# Accessing the balance through the property
print("Initial Balance:", account.balance)

# Updating the balance using the setter
account.balance = 1500
print("Updated Balance:", account.balance)

# Trying to set a negative balance (setter won't allow it)
account.balance = -500
print("Balance after invalid update:", account.balance)


# Example 3: Using Protected Attributes

class Employee:
    def __init__(self, name, _salary):  # protected attribute
        self.name = name
        self._salary = _salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}")


# Creating an instance of the Employee class
employee = Employee("John Doe", 50000)

# Accessing protected attribute directly (not recommended, but possible)
print("Salary:", employee._salary)

# Accessing the attribute through a method
employee.display_info()
