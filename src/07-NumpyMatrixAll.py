from numpy import *

A = array([arange(1, 4), arange(4, 7), arange(7, 10)])
B = array([[2, 0, 1], [-2, 3, 4], [-5, 5, 6]])

# 두 행렬을 비교
isSameMatrix = (A is B)
print("isSameMatrix :", isSameMatrix)

# A 행렬에 대한 스칼라 곱 (나눗셈도 가능)
scalarResult = A * 10.0
print("scalarResult :\n", scalarResult)

# 두 행렬의 각 성분에 대한 합
add = A + B
print("add :\n", add)

# 두 행렬의 각 성분에 대한 차
sub = A - B
print("sub :\n", sub)

# 두 행렬의 각 성분에 대한 곱
mul = A * B
print("mul :\n", mul)

# A 행렬에 대한 전치 행렬
transposeResult = transpose(A)
print("transpose :\n", transposeResult)

# B 행렬에 대한 역행렬
inverseResult = linalg.inv(B)
print("inverseResult :\n", inverseResult)

# 두 행렬의 곱 : AB
dotResultAB = dot(A, B) # same with A.dot(B)
print("dotResultAB :\n", dotResultAB)

# 두 행렬의 곱 : BA
dotResultBA = dot(B, A) # same with B.dot(A)
print("dotResultBA :\n", dotResultBA)

# B 행렬의 행렬식
det = linalg.det(B)
print("det :", det)
