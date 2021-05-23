
# 4주차 1차시

from numpy import array, linspace, zeros, sign, cos
import matplotlib.pyplot as plt


def f(x):
    return -x ** 2 + 6.0 * x - 5.0


a = -2.0
b = 3.0
n = 7
c = zeros(n)
x = array([1, 2, 3, 4, 5, 6, 7])

for i in range(n):
    c[i] = (a + b) / 2.0
    if sign(f(c[i])) == sign(f(a)):
        a = c[i]
    else:
        b = c[i]

print('%5s %4s %9s' % ('k', 'c', 'e',))

e = zeros(n)
for i in range(n - 1):
    e[i + 1] = abs((c[i + 1] - c[i]) / c[i + 1])

for k in range(n):
    print('%5d %9.4f %9.4f' % (k + 1, c[k], e[k]))

print('\t근사해: %.4f' % c[n - 1])

plt.plot(x, c, 'ko-')
plt.plot(x, e, 'bo-')
plt.show()
