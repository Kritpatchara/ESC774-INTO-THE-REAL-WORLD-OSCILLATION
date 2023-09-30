import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def para(x,c0,c1,c2):
  return c2*x**2 + c1*x + c0

xdata = np.arange(0,10,1)
ydata = 4*xdata**2

ydata[2] += 1.5
ydata[6] += -3

[popt, pcov] = curve_fit(para,xdata,ydata)

#print(xdata)
#print(ydata)

# optimized values of m and c
print(popt)
c0_fit = popt[0]
c1_fit = popt[1]
c2_fit = popt[2]

# model plotting
xfit = np.arange(0,10,0.01)
yfit = para(xfit,c0_fit,c1_fit,c2_fit) # linear(x,m,c)

plt.scatter(xdata,ydata,label='raw data')
plt.plot(xfit,yfit,'r',label='model')
plt.legend()
plt.show()