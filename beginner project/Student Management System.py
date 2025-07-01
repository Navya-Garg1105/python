class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_number, name, marks):
        for student in self.students:
            if student.roll_number == roll_number:
                return "Error: Roll number already exists."
        self.students.append(Student(roll_number, name, marks))
        return "Student added successfully."

    def display_students(self):
        if not self.students:
            return "No students found."
        return "\n".join(str(student) for student in self.students)

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return str(student)
        return "Student not found."

def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add a Student")
        print("2. Display All Students")
        print("3. Search for a Student by Roll Number")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                roll_number = int(input("Enter roll number: "))
                name = input("Enter name: ")
                marks = float(input("Enter marks: "))
                print(system.add_student(roll_number, name, marks))
            except ValueError:
                print("Invalid input. Please enter correct details.")

        elif choice == 2:
            print("\nStudent Details:")
            print(system.display_students())

        elif choice == 3:
            try:
                roll_number = int(input("Enter roll number to search: "))
                print(system.search_student(roll_number))
            except ValueError:
                print("Invalid input. Please enter a numeric roll number.")

        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
