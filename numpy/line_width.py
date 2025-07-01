import matplotlib.pyplot as plt 
Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
Stock_Value = [100, 105, 102, 108, 110]

plt.plot(Days, Stock_Value, marker = 'o', linewidth = 3, color='purple')
plt.title("Stock Market Variation")
plt.xlabel('Days')
plt.ylabel('Stock Value')
plt.show()