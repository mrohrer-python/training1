import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 5, 6, 2])
ypoints = np.array([3,8,1,10, 4])

#plt.plot(xpoints, ypoints)
#plt.plot(xpoints, ypoints, '*-y') # '*-y' 'o:m' '+-.g'
plt.plot(xpoints, ypoints, 'D', ms=20, mec='g', mfc='r')
#plt.plot(ypoints)

plt.show()