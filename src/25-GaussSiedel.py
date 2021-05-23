from numpy import zeros
import matplotlib.pyplot as plt

m = 8
x1 = zeros(m)
x2 = zeros(m)
x3 = zeros(m)
e1 = zeros(m)
e2 = zeros(m)
e3 = zeros(m)
it = range(m)

print('%7s %9s %9s %9s %9s %9s %9s' % ('k', 'x1', 'x2', 'x3', 'e1', 'e2', 'e3'))
print('%7d %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' %
      (0, x1[0], x2[0], x3[0], e1[0], e2[0], e3[0]))

for k in range(m - 1):
    x1[k + 1] = (-1.0 + 2.0 * x2[k] - 3.0 * x3[k]) / 5.0
    x2[k + 1] = (2.0 + 3.0 * x1[k+1] - x3[k]) / 9.0
    x3[k + 1] = (-3.0 + 2.0 * x1[k+1] - x2[k+1]) / 7.0

    e1[k + 1] = abs(x1[k + 1] - x1[k]) / abs(x1[k + 1])
    e2[k + 1] = abs(x2[k + 1] - x2[k]) / abs(x2[k + 1])
    e3[k + 1] = abs(x3[k + 1] - x3[k]) / abs(x3[k + 1])

    print('%7d %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' %
          (k + 1, x1[k + 1], x2[k + 1], x3[k + 1], e1[k + 1], e2[k + 1], e3[k + 1]))

plt.plot(it, x1, 'ko-', label='x1')
plt.plot(it, x2, 'bo-', label='x2')
plt.plot(it, x3, 'go-', label='x3')
plt.plot(it, e1, 'k--', label='e1')
plt.plot(it, e2, 'b--', label='e2')
plt.plot(it, e3, 'g--', label='e3')
plt.legend()
plt.xlabel('iteration')
plt.ylabel('Approximate Solutions')
plt.show()
