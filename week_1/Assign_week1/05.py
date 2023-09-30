import numpy as np
x = float(input("Number: "))
d = np.abs(x-17)
if x > 17:
    print(2*np.abs(d))
else:
    print(d)