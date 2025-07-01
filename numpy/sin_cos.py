import matplotlib.pyplot as plt
import numpy as np
x_data = np.linspace(0, 2*np.pi, 100)
y_data1 = np.sin(x_data)
y_data2 = np.cos(x_data)

plt.subplot(221)
plt.plot(x_data, y_data1)

plt.subplot(222)
plt.plot(x_data, y_data2)

plt.subplot(223)
plt.plot(x_data, y_data1, color = 'red')

plt.subplot(224)
plt.plot(x_data, y_data1, color = 'green')

plt.show()

