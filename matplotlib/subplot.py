import matplotlib.pyplot as plt
Students = [1, 2, 3, 4, 5]
Attendance = [90, 85, 80, 95, 70]
Marks = [88, 75, 70, 95, 60]
plt.subplot(221)
plt.plot(Students, Attendance, color='red', marker = 'o')
plt.xlabel("Students")
plt.ylabel("Attendance")
plt.subplot(222)
plt.plot(Students,Marks, color='green', marker = 'o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()