
# 4주차 2차시

from numpy import zeros, array, cos
import matplotlib.pyplot as plt


def g(x):
    return 1.0 / 3.0 * (cos(x) + 1.0)


n = 10
x0 = 1.0
x = zeros(n)
x[0] = x0
it = array(range(1, n + 1))

for i in range(n - 1):
    x[i + 1] = g(x[i])

print('%5s %4s %9s' % ('k', 'x', 'e',))

e = zeros(n)
for i in range(n - 1):
    e[i + 1] = abs((x[i + 1] - x[i]) / x[i + 1])

for k in range(n):
    print('%5d %9.4f %9.4f' % (k + 1, x[k], e[k],))

print('\t근사해: %.4f' % x[n - 1])

plt.plot(it, x, 'ko-')
plt.plot(it, e, 'bo-')
plt.show()
