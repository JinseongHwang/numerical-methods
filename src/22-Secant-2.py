
# 5주차 2차시

from numpy import zeros, array, linspace, cos
import matplotlib.pyplot as plt


def f(x):
    return 3 * x - cos(x) - 1.0


n = 7
xs = zeros(n)
x0 = -2.0
x1 = 3.0
it = list(range(0, 7))

for k in range(n):
    x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    x0 = x1
    x1 = x2
    xs[k] = x2

# printing output
print('%5s %4s %9s' % ('k', 'x', 'e',))

e = zeros(n)
for i in range(n - 1):
    e[i + 1] = abs((xs[i + 1] - xs[i]) / xs[i + 1])

for k in range(n):
    print('%5d %9.4f %9.4f' % (k + 1, xs[k], e[k]))

print('\t근사해: %.4f' % xs[n - 1])

plt.plot(it, xs, 'ko-')
plt.plot(it, e, 'bo-')
plt.show()
