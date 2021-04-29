import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 6, 2])
y = np.array([3, 8, 5, 10, 4])
plt.subplot(2, 2, 1)
plt.plot(x, y)

x = np.array([3, 6, 5, 4, 1])
y = np.array([3, 5, 1, 8, 4])
plt.subplot(2, 2, 2)
plt.plot(x, y)

x = np.array([1, 3, 5, 6, 2])
y = np.array([3, 8, 1, 10, 4])
plt.subplot(2, 2, 3)
plt.plot(x, y)

y4 = np.array([12, 6, 10, 9])
labels =["Kunde A", "Kunde B", "Kunde C", "Kunde D"]
special = [0.1, 0, 0, 0]
plt.subplot(2, 2, 4)
plt.pie(y4, labels=labels, explode=special, shadow=True)


plt.show()