from numpy import linspace
import matplotlib.pyplot as plt

x = linspace(-100, 100, 1000)
y = (-x ** 2) - (6 * x) - 5

plt.plot(x, y, 'k-', label='-x^2 -6x -5')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
