from numpy import array, linspace
import matplotlib.pyplot as plt


def f(arg):
    return arg / 2.0 + (3.0 / 2.0)


x = array([0, 1, 2])
y = array([1, 3, 2])

xspace = linspace(0, max(x), 5)

plt.scatter(x, y, s=90, facecolor='black', label='Data')
plt.plot(xspace, f(xspace), 'k--', label='Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
