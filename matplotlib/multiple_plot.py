import matplotlib.pyplot as plt 
Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
A =  [22, 24, 19, 23, 25]
B = [18, 20, 17, 21, 22]
plt.plot(Days, A, color = 'green', marker = 'o', label = 'A')
plt.plot(Days, B, color = 'blue', marker = 'o', label = 'B')
plt.xlabel('Days')
plt.ylabel("temperature (C)")
plt.grid()
plt.show()
