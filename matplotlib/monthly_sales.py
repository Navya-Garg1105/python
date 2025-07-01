import matplotlib.pyplot as plt 
Months = ['Jan', 'Feb', 'Mar', 'Apr']
Sales =  [2500, 2700, 3000, 2800]
plt.bar(Months, Sales, color = 'purple')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
