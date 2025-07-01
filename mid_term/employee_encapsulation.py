class Employee:
    def __init__(self, name, salary):
        self.__name = name      # Private attribute
        self.__salary = salary  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:  # Ensuring salary is not negative
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

# Example usage:
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))

emp = Employee(name, salary)

print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: {emp.get_salary()}")

# Modifying employee details
new_name = input("Enter new name: ")
emp.set_name(new_name)

new_salary = float(input("Enter new salary: "))
emp.set_salary(new_salary)

print(f"Updated Employee Name: {emp.get_name()}")
print(f"Updated Employee Salary: {emp.get_salary()}")
