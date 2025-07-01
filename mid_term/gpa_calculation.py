class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    
    def add_course(self, credit, grade):
        self.courses.append((credit, grade))
    
    # Implement this method
    def calculate_gpa(self):
        # Logic here
        total_credit = 0
        total_point = 0
        grades = { 'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
        for credit, grade  in self.courses:
            if grade in grades:
                total_credit += credit
                total_point += (credit * grades[grade])
        if total_credit == 0:
            return 0.0
        gpa = total_point/total_credit
        return round(gpa, 2)
# Test Input
student = Student("Alice")
student.add_course(3, 'A')
student.add_course(4, 'B')
print(f"{student.calculate_gpa():.2f}")  # Expected Output: 3.14