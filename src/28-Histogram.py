from numpy import array, histogram
import matplotlib.pyplot as plt

height = array([8.2, 8.1, 9.1, 6.3, 7.6, 8.1, 6.5, 5.5, 9.1, 8.3])
bins = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

histo = histogram(height)
hist_value = array(histo)
print(hist_value)

plt.hist(height, bins, rwidth=0.8, alpha=0.5)

plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()
