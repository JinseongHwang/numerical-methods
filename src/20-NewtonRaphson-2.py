
# 5주차 1차시

from numpy import zeros, array, cos, sin
import matplotlib.pyplot as plt


def f(x):
    return 3 * x - cos(x) - 1


def df(x):
    return 3 + sin(x)


n = 7
x0 = 0.0
x = zeros(n)
x[0] = x0
it = list(range(0, 7))

for k in range(n - 1):
    x[k + 1] = x[k] - f(x[k]) / df(x[k])

# printing output
print('%5s %4s %9s' % ('k', 'x', 'e',))

e = zeros(n)
for i in range(n - 1):
    e[i + 1] = abs((x[i + 1] - x[i]) / x[i + 1])

for k in range(n):
    print('%5d %9.4f %9.4f' % (k + 1, x[k], e[k]))

print('\t근사해: %.4f' % x[n - 1])

plt.plot(it, x, 'ko-')
plt.plot(it, e, 'bo-')
plt.show()
