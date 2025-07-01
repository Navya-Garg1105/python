import matplotlib.pyplot as plt 
Days = [1, 2, 3, 4, 5]
Height = [2, 3, 5, 7, 11]

plt.plot(Days, Height, marker = 'o', color = 'green')
plt.title("growth")
plt.xlabel("Days")
plt.ylabel("Height")
plt.grid()
plt.show()
