import numpy as np
import matplotlib.pyplot as plt

m = float(input("Input mass: "))
v = float(input("Input initial speed: "))
k = float(input("Input k constant: "))
x = 0
h = 0.001
i = 0
t = 0
x_list = []
v_list = []
t_list = []
while i <= 50000:
  F = -k * x
  x = x + v*h + 0.5*(F/m)*(h**2)
  v = v + (F/m)*h
  t = t + h
  i += 1
  if i % 100 == 0:
    x_list.append(x)
    v_list.append(v)
    t_list.append(t)

plt.scatter(t_list, x_list)
plt.show()