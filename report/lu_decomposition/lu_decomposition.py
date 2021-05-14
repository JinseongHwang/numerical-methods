from numpy import array, dot, zeros, concatenate, transpose
from copy import deepcopy

N = 0
A = []
L = []
U = []
b = []
print_data = ''


def print_lu():
    global print_data
    print_data += '===== L =====\n'
    print_data += str(L)
    print_data += '\n===== U =====\n'
    print_data += str(array(U))


def file_input(file_path):
    file = open(file_path)
    file_content = file.readlines()
    for idx, line in enumerate(file_content):
        if idx == 0:
            global N
            N = int(line.strip().split()[0])
        else:
            curr_list = list(map(int, line.strip().split()))
            b.append([array(curr_list[-1])])
            A.append(curr_list[:-1])

    file.close()


def file_output(file_path):
    file = open(file_path, 'w')
    file.writelines(print_data)
    file.close()


def lu_decomposition(matrix):
    if len(matrix) == len(matrix[0]):
        dimension = len(matrix)
        L = zeros((dimension, dimension))
    else:
        print("정방행렬이 아닙니다.")
        return

    while matrix[0][0] == 0:  # swap
        tmp = deepcopy(matrix[0])
        matrix[0] = deepcopy(matrix[1])
        matrix[1] = deepcopy(tmp)

    U = deepcopy(matrix)

    idx = 0
    for col in range(dimension):
        for row in range(dimension):
            idx += U[row][col]
        if idx == 0:
            print(col + 1, "열 의 값이 모두 0입니다.")
            return

    for i in range(dimension):
        product = deepcopy(U[i][i])
        if product == 0:
            continue
        else:
            L[i][i] = product
            U[i] = [v / product for v in U[i]]
            for j in range(i + 1, dimension):
                sum = deepcopy(U[j][i])
                L[j][i] = sum
                for idx in range(len(U[i])):
                    U[j][idx] -= sum * deepcopy(U[i][idx])

    return L, U


def get_y():
    Lb = concatenate((L, array(b)), axis=1)
    m = len(Lb[0])
    for col in range(m - 1):
        for row in range(col + 1, m - 1):
            const = Lb[row][col] / Lb[col][col] * -1
            Lb[row] += const * Lb[col]

    for i in range(m - 1):
        Lb[i] /= Lb[i][i]

    return Lb[:, -1].reshape(1, -1)


def get_x(y):
    Ux = concatenate((U, y.T), axis=1)

    m = len(Ux[0])
    for col in range(m - 2, 0, -1):
        for row in range(col - 1, -1, -1):
            const = Ux[row][col] / Ux[col][col] * -1
            Ux[row] += const * Ux[col]

    for i in range(m - 1):
        Ux[i] /= Ux[i][i]

    return Ux[:, -1]


def print_result(x):
    global print_data
    for idx, v in enumerate(x):
        print_data += f'\nx{idx} = {v}'


def run():
    global L, U
    L, U = lu_decomposition(A)
    print_lu()
    y = get_y()
    x = get_x(y)
    print_result(x)
    return print_data

# file_input(None)
# print(run())

#
# def main():
#     file_input()
#     L, U = lu_decomposition(mat)
#     print(L)
#     print(array(U))
#
#
# if __name__ == '__main__':
#     main()
