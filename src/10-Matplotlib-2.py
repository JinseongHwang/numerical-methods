from numpy import linspace, cos, sin, pi
import matplotlib.pyplot as plt

x = linspace(0, 2.0 * pi, 40)
yc = cos(x)
ys = sin(x)

plt.plot(x, yc, 'r-', label='cos(x)')
plt.plot(x, ys, 'b-', label='sin(x)')
plt.legend()  # 범례, 카테고리
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = cos(x) & sin(x)')
plt.show()
