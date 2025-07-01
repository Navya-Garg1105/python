import matplotlib.pyplot as plt

# Data
Months = [1, 2, 3, 4, 5, 6]
City1_Temp = [30, 32, 35, 37, 40, 42]
City2_Temp = [20, 22, 24, 27, 30, 33]

# Plotting
plt.plot(Months, City1_Temp, color='yellow', marker='o', label='City 1')
plt.plot(Months, City2_Temp, color='blue', marker='s', label='City 2')

# Labels and title
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Comparison')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
