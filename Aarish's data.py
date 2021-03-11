# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:33:04 2021

@author: matte
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1.96,1.96,1.96,1.95,1.92,1.89,1.82,1.73,1.67,1.5])#vAccross
y = np.array([4.68,4.68,4.68,4.4,4,3.252,2.58,1.9,0.596,0.21])#light intensity
plt.xlabel("Voltage Actual Readings")#names the axis
plt.ylabel("Light intensity")#names the axis
plt.scatter(x, y, color = 'red')
a= np.array([2.07,2.05,2.01,1.97,1.95,1.92,1.87,1.8,1.7,1.6])#vAccross
b= np.array([0.71,0.6,0.47,0.356,0.252,0.165,0.104,0.078,0.078,0.078])#light intensity
plt.scatter(a, b, color = 'green')
plt.show()
