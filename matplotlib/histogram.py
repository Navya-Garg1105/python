import matplotlib.pyplot as plt
ages = [22, 25, 30, 22, 29, 40, 35, 25, 28, 30, 32, 40, 22]
bins = [20, 25, 30, 35, 40, 45]  
plt.hist(ages, bins=bins, edgecolor='black', color='skyblue', rwidth = 0.8)
plt.title('Age Distribution of Workshop Attendees')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.xticks(bins)
plt.show()
