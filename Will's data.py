import numpy as np
import matplotlib.pyplot as plt
x = np.array([2.002,2,1.998,1.976,1.904,1.865,1.826,1.786,1.733,1.672])
y = np.array([6,5.76,5.724,5.364,3.693,2.860,2.096,1.308,0.556,0.160])
plt.xlabel("Voltage Actual Readings")#names the axis
plt.ylabel("Light intensity")#names the axis
plt.scatter(x, y, color = 'red')
a= np.array([2.075,2.072,2.068,2.06,2.01,1.982,1.952,1.915,1.865,1.787])
b= np.array([0.39,0.386,0.38,0.36,0.252,0.198,0.146,0.102,0.072,0.062])
plt.scatter(a, b, color = 'green')
plt.show()