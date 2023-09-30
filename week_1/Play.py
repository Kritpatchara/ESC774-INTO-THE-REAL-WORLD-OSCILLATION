import numpy as np
import matplotlib.pyplot as plt

d = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.450, 0.500, 0.500, 0.630, 0.800, 0.900, 0.900, 0.900, 0.900, 1.000, 1.100, 1.100, 1.400, 1.700, 2.000, 2.000, 2.000, 2.000])
v = np.array([170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090])

# Calculate the trend line
z = np.polyfit(d, v, 1)
p = np.poly1d(z)

# Create a scatter plot of the data
plt.scatter(d, v, label='Data')

# Create a line plot for the trend line
plt.plot(d, p(d), color='red', label='Trend Line')

# Set the plot labels and title
plt.xlabel('Distance')
plt.ylabel('Velocity')
plt.title('Trend Line of Distance vs Velocity')

# Show the legend
plt.legend()

# Display the plot
plt.show()