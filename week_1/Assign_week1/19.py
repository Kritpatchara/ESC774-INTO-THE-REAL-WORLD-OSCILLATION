import numpy as np
import matplotlib.pyplot as plt

g = 9.81
u = float(input("Initial speed (m/s): "))
theta = float(input("Initial speed(degree): "))
theta_rad = theta/180*np.pi

t = np.arange(0, 1, 0.01)
x = u*np.cos(theta_rad)*t
y = u*np.sin(theta_rad)*t - 0.5*g*t**2

plt.plot(x, y)
plt.show()