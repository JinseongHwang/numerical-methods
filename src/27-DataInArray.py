from numpy import mean, median, var, std, array

x = array([20, 23, 25, 22, 21, 19, 18])

mean_temp = mean(x)  # 평균
median_temp = median(x)  # 중앙값
variance_temp = var(x)  # 분산
standard_deviation_temp = std(x)  # 표준편차

print('mean = %6.2f' % mean_temp)
print('median = %6.2f' % median_temp)
print('variance = %6.2f' % variance_temp)
print('standard deviation = %6.2f' % standard_deviation_temp)
