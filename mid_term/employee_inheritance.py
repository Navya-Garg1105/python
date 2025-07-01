class Employee:
    def __init__(self, name, base_salary):
        self.name  = name 
        self.base_salary = base_salary

    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.bonus + self.base_salary
        print(f"{total_salary} is paid to Manager")

class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, overtime_rate):
        super().__init__(name, base_salary)
        self.hrs = overtime_hours
        self.rate = overtime_rate

    def calculate_salary(self):
        total_salary = self.base_salary + self.hrs + self.rate
        print(f"{total_salary} is paid to Devloper")

# Example usage:
# Read input and create objects
manager = Manager("Alice", 50000, 10000)
developer = Developer("Bob", 40000, 10, 500)

manager.calculate_salary()  # Manager Alice's total salary: 60000
developer.calculate_salary()  # Developer Bob's total salary: 45000