from numpy import array, linspace, zeros, sign, cos
import matplotlib.pyplot as plt


def f(x):
    return 3 * x - cos(x) - 1.0


a = 0.0
b = 5.0
n = 15
c = zeros(n)
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

for i in range(n):
    c[i] = (a + b) / 2.0
    if sign(f(c[i])) == sign(f(a)):
        a = c[i]
    else:
        b = c[i]

print('%5s %8s' % ('k', 'c',))

for k in range(n):
    print('%5d %9.4f' % (k + 1, c[k],))

plt.plot(x, c, 'ko-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
