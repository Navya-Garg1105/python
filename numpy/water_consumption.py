import matplotlib.pyplot as plt
Months = [1, 2, 3, 4, 5, 6]
Consumption = [300, 280, 290, 310, 320, 330]

plt.plot(Months, Consumption, color = 'brown',marker='s')
plt.title('Water Consumption each month')
plt.xlabel('Months')
plt.ylabel('Consumption')
plt.grid()
plt.show()