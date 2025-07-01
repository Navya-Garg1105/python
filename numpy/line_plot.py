import matplotlib.pyplot as plt

# Data
Years = [2016, 2017, 2018, 2019, 2020]
Profit = [100, 120, 150, 180, 200]

# Plot
plt.plot(Years, Profit, color='green', linestyle='--')  
plt.xlabel('Year')
plt.ylabel('Profit')
plt.title('Company Profit Trend')
plt.grid(True)

# Show the plot
plt.show()
