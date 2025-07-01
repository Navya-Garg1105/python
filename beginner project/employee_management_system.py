# EMPLOYEE MANAGEMENT SYSTEM

class employee:
    def __init__(self,name,emp_id,deptt,salary):
        self.name = name
        self.emp_id = emp_id
        self.deptt = deptt
        self.salary = salary
    def display_info(self):
        return f'''Name : {self.name}
Employee Id : {self.emp_id}
Department : {self.deptt}
salary : {self.salary}'''
        
    def update_info(self, name=None, deptt=None, salary=None):
        if name:
            self.name = name 
        if deptt:
            self.deptt = deptt
        if salary:
            self.salary = salary
    def increment_salary(self, perc):
        self.salary += (perc/100) * self.salary
class employee_management:


    def __init__(self):
        self.reg = {}

    def add_employee(self,name,emp_id,deptt,salary):
        if emp_id in self.reg:
            print("employee id already exist")
            print('check details try with different employee ID')
            print('Already filled details')
            print(self.reg[emp_id].get_details())
        else:
            self.reg[emp_id] = employee(name,emp_id,deptt,salary)
            print(f'employee id {emp_id} successfully created')

    def display_all_employee(self):
        for emp in self.reg:
            self.reg[emp].display_info()

    def increment_salary(self, id,increment_percentage):
        for emp  in self.reg.values():
            emp.increment_salary(increment_percentage)
            print(f'salary of {emp.name} incresed by {increment_percentage }% . \n new salary: {emp.salary}')   

system = employee_management()
while True:
    # main code 
    print('\n welcome to gla university')
    print('\nAvailable choices')
    print("""
    1.add employees
    2. increase salary
    3. display all employees
    4. delete employee by ID
    5. salary increment by ID
    6. exit""")
    choice = int(input('enter the choice'))
    if choice == 1:
        e_id = input('enter the employee id')
        name = input("enter the employee name")
        deptt = input('enter the employee department')
        salary = int(input('enter the salary'))

        system.add_employee(e_id, name, deptt, salary)

    elif choice == 2:
        id = input("enter the employee id to increase the salary")
        perc = int(input("enter the percentage increase in salary"))
        system.increment_salary(id,perc)

    elif choice == 3:
        system.display_all_employee()
    
    elif choice == 4:
        pass
