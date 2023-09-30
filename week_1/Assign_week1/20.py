import numpy as np
import matplotlib.pyplot as plt

g = 9.81

print("First")
u1 = float(input("Initial speed (m/s): "))
theta1 = float(input("Initial angle (degree): "))
theta_rad1 = theta1/180 * np.pi

t1 = np.arange(0, 1, 0.01)
x1 = u1 * np.cos(theta_rad1) * t1
y1 = u1 * np.sin(theta_rad1) * t1 - 0.5 * g * t1**2

print("\nSecond")
u2 = float(input("Initial speed (m/s): "))
theta2 = float(input("Initial angle (degree): "))
theta_rad2 = theta2/180 * np.pi

t2 = np.arange(0, 1, 0.01)
x2 = u2 * np.cos(theta_rad2) * t2
y2 = u2 * np.sin(theta_rad2) * t2 - 0.5 * g * t2**2

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.show()