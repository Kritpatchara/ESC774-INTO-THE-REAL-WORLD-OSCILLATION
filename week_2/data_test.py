import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, c):
    return m*x + c

xdata = np.arange(0, 10, 1)
ydata = 4*xdata

[popt, pcov] = curve_fit(linear, xdata, ydata)

print(popt)
m_fit = popt[0]
c_fit = popt[1]

xfit = np.arange(0, 10, 0.01)
yfit = linear(xfit, m_fit, c_fit)


import numpy as np
data_to_write = np.column_stack((xdata, ydata))
np.savetxt("data01.txt", data_to_write)
np.savetxt("data02.txt", data_to_write, fmt = "%8.3f")
np.savetxt("data03.csv", data_to_write, fmt = "%8.3f", delimiter = ",")

data_read01 = np.genfromtxt("data01.txt")
print(data_read01)