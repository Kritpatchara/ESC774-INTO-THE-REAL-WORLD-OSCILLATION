import numpy as np
import matplotlib.pyplot as plt
1
# y axis = sin(x)
# x axis = x

#define arrays for x and y axis
x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()