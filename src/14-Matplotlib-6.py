from numpy import linspace, cos
import matplotlib.pyplot as plt

x = linspace(-100, 100, 1000)
y = (3 * x) - cos(x) - 1

plt.plot(x, y, 'k-', label='3x -cos(x) -1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
