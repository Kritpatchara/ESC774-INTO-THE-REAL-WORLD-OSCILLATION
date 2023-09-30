# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:20:16 2021

@author: Teerasit
"""

import numpy as np
import matplotlib.pyplot as plt

R = [2]
J = [-10]
a = -1
b = 2
dt = 0.01

for i in range(0,100):
    
    R1 = ((a * R[i] + b * J[i]) * dt) + R[i]
    J1 = ((b * R[i] + a * J[i]) * dt) + J[i]
    
    R.append(R1)
    J.append(J1)
    
plt.plot(R)
plt.plot(J)
plt.show()