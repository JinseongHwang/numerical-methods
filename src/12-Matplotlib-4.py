import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2

# scatter는 산점도를 표현할 때 사용한다.
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
