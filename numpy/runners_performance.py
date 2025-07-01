import matplotlib.pyplot as plt

# Data
Days = [1, 2, 3, 4, 5, 6, 7]
Distance = [2, 3, 5, 6, 5, 7, 8]

# Plot
plt.plot(Days, Distance, color='blue', marker='o')  # blue line with circle markers
plt.xlabel('Day')
plt.ylabel('Distance Run (km)')
plt.title("Runner's Performance Over a Week")
plt.grid()

# Show the plot
plt.show()
