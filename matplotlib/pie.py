import matplotlib.pyplot as plt
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
votes = [40, 25, 20, 15]
plt.pie(votes, labels=fruits, autopct='%.2f', startangle=140)
plt.title('Favorite Fruits Survey')
plt.axis('equal')
plt.show()
