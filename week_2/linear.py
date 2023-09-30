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

plt.scatter(xdata, ydata, label = "raw data")
plt.plot(xfit, yfit, "r", label ="model")
plt.legend
plt.show()