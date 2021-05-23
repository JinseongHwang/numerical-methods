from numpy import zeros
import matplotlib.pyplot as plt

m = 10
x1j = zeros(m)
x2j = zeros(m)
x3j = zeros(m)
e1 = zeros(m)
e2 = zeros(m)
e3 = zeros(m)
it = range(m)

print('%7s %9s %9s %9s %9s %9s %9s' % ('k', 'x1', 'x2', 'x3', 'e1', 'e2', 'e3'))
print('%7d %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' %
      (0, x1j[0], x2j[0], x3j[0], e1[0], e2[0], e3[0]))

for k in range(m - 1):
    x1j[k + 1] = (-1.0 + 2.0 * x2j[k] - 3.0 * x3j[k]) / 5.0
    x2j[k + 1] = (2.0 + 3.0 * x1j[k] - x3j[k]) / 9.0
    x3j[k + 1] = (-3.0 + 2.0 * x1j[k] - x2j[k]) / 7.0

    e1[k + 1] = abs(x1j[k + 1] - x1j[k]) / abs(x1j[k + 1])
    e2[k + 1] = abs(x2j[k + 1] - x2j[k]) / abs(x2j[k + 1])
    e3[k + 1] = abs(x3j[k + 1] - x3j[k]) / abs(x3j[k + 1])

    print('%7d %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' %
          (k + 1, x1j[k + 1], x2j[k + 1], x3j[k + 1], e1[k + 1], e2[k + 1], e3[k + 1]))

plt.plot(it, x1j, 'ko-', label='x1')
plt.plot(it, x2j, 'bo-', label='x2')
plt.plot(it, x3j, 'go-', label='x3')
plt.plot(it, e1, 'k--', label='e1')
plt.plot(it, e2, 'b--', label='e2')
plt.plot(it, e3, 'g--', label='e3')
plt.legend()
plt.xlabel('iteration')
plt.ylabel('Approximate Solutions')
plt.show()
