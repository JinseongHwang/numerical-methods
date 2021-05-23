from numpy.linalg import det
import copy

A_ = []
MAT_SIZE = 0

A = []
x = []
b = []


def init_mat_size(size):
    # 행렬의 크기 N을 초기화한다.
    global MAT_SIZE
    MAT_SIZE = size


def init_x():
    global x
    x = [0 for _ in range(MAT_SIZE)]


def file_input():
    # 행렬을 파일을 통해 입력받는다.
    f = open('../test_data/test_data(A).txt', 'r')
    lines = f.readlines()
    init_mat_size(len(lines))
    init_x()
    for i in range(MAT_SIZE):
        line = lines[i]
        int_line = list(map(int, line.strip().split()))
        A.append(int_line)

    f = open('../test_data/test_data(b).txt', 'r')
    lines = f.readlines()
    for i in range(MAT_SIZE):
        line = lines[i]
        b.append(int(line.strip().split()[0]))


def set_sub_A():
    # a1, a2, ... 를 영행렬 형태로 생성한다.
    global A_
    A_ = [copy.deepcopy(A) for _ in range(MAT_SIZE)]

    #
    change_col = 0
    for sub in A_:
        b_idx = 0
        for row in sub:
            row[change_col] = b[b_idx]
            b_idx += 1
        change_col += 1


def cramer():
    # 행렬식 연산 완료
    det_A = det(A)
    det_sub = []
    for sub in A_:
        det_sub.append(det(sub))

    for i, det_s in enumerate(det_sub):
        print(f'x{i + 1} = {det_s / det_A}')


def main():
    file_input()
    set_sub_A()
    cramer()


if __name__ == '__main__':
    main()

"""
3x3 예제
A = 
1 4 2
0 2 1
3 5 3

b =
1
-1
2
"""