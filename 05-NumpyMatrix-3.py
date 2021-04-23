from numpy import *

# 행렬끼리 연산
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = array([[-1, 1, 2], [5, 4, 2], [3, 1, -2]])

mAdd = A + B
mSub = A - B
mMul = A * B

print(A)
print(B)
print('---')

print(mAdd)
print(mSub)
print(mMul)
