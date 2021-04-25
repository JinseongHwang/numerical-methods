from numpy import linspace, zeros, cos

# 벡터화 기법 적용 전
#
# x = linspace(0, 2, 10)
# n = len(x)
# y = zeros(n)
#
# for i in range(n):
#     y[i] = cos(x[i])
#     print('%8.4f ' % (y[i]))


# 벡터화 기법 적용 후
# 불필요한 반복문을 생략할 수 있다.
#
x = linspace(0, 2, 10)
y = cos(x)
print(y)
