# component class 
class employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display_info(self):
        print(f"name : {self.name} \nemployee id : {self.emp_id} \nsalary : {self.salary}")
# container class
class management:
    def __init__(self,emp1):
        self.emp = emp1 # has a relationship
    def add_employee(self,emp):
        self.emp[emp.emp_id] = emp # has a relationship with type composition
emp1 = employee('Ravi','gla123',25000)
system = management(emp1)
system.emp.display_info()