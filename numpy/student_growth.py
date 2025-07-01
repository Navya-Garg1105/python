import matplotlib.pyplot as plt

# Data
Years = [2018, 2019, 2020, 2021, 2022]
Marks = [65, 70, 72, 78, 85]

# Plot
plt.plot(Years, Marks, color='red', marker='o')  # red colored line with markers
plt.xlabel('Year')
plt.ylabel('Marks')
plt.title('Student Marks Growth')
plt.grid(True)

# Show the plot
plt.show()
