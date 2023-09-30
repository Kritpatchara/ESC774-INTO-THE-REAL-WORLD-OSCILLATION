import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def damped(t, x0, A0, gamma, period, phase):
    return x0 + A0 * np.exp(-gamma * t) * np.sin(2 * np.pi / period * t + phase)


data = np.genfromtxt(
    "D:\Code\KMUTT\ESC 5C\ESC774_Into_the_real_world_osciallation\week_2\data_assign.txt", skip_header=2, delimiter=',')

tdata = data[:, 0]
xdata = data[:, 1]

x0_guess = 0.02
A0_guess = 0.025
gamma_guess = 0
period_guess = 1
phase_guess = 0

[popt, pcov] = curve_fit(damped, tdata, xdata, p0=[
                         x0_guess, A0_guess, gamma_guess, period_guess, phase_guess])

x0_fit = popt[0]
A0_fit = popt[1]
gamma_fit = popt[2]
period_fit = popt[3]
phase_fit = popt[4]

print(popt)
print(np.mean(xdata))
t_fit = np.arange(0, 6, 0.01)
x_fit = damped(t_fit, x0_fit, A0_fit, gamma_fit, period_fit, phase_fit)

plt.scatter(tdata, xdata, label="raw")
plt.plot(t_fit, x_fit, "r", label="model")
plt.legend()
plt.show()

 dataB = np.genfromtxt(
     "D:\Code\KMUTT\ESC 5C\ESC774_Into_the_real_world_osciallation\week_2\data_assignB.txt", skip_header=2, delimiter=',')
 tdataB = dataB[:, 0]
 xdataB = dataB[:, 1]

 x0_guessB = 0.02
 A0_guessB = 0.025
 gamma_guessB = 0
 period_guessB = 1
 phase_guessB = 0

 [popt, pcov] = curve_fit(damped, tdataB, xdataB, p0=[
                          x0_guessB, A0_guessB, gamma_guessB, period_guessB, phase_guessB])

 x0_fitB = popt[0]
 A0_fitB = popt[1]
 gamma_fitB = popt[2]
 period_fitB = popt[3]
 phase_fitB = popt[4]

 print(popt)

 t_fitB = np.arange(0, 6, 0.01)
 x_fitB = damped(t_fitB, x0_fitB, A0_fitB, gamma_fitB, period_fitB, phase_fitB)

 plt.scatter(tdata, xdata, label="raw")
 plt.plot(t_fit, x_fit, "r", label="model")
 plt.legend()
 plt.scatter(tdataB, xdataB, label="raw2")
 plt.plot(t_fitB, x_fitB, "r", label="model2")
 plt.legend()
 plt.show()

