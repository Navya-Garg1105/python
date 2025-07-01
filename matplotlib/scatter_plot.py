import matplotlib.pyplot as plt
students = [1, 2, 3, 4, 5]
marks = [88, 92, 75, 85, 90]
plt.scatter(students, marks, color='blue', marker='o')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks in Math')
plt.grid(True)
plt.show()
