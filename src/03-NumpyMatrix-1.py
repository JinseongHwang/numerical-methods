from numpy import *

mat = array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(mat)
print(mat.shape)

print('---')

rng1 = arange(5)  # array range를 편하게 생성해주는 함수
rng2 = arange(1, 10, 3)
print(rng1)
print(rng2)

print('---')
space = linspace(0, 1, 5)  # linear space 생성 (start, end, N)
# N: 숫자의 개수 -> 구간의 개수는 N-1개이다.
print(space)
