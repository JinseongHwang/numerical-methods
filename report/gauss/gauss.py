from numpy import array
from copy import deepcopy

N = 0
mat = []
print_data = ''


def print_matrix():
    numpy_mat = array(mat)
    # print((str(numpy_mat)))
    global print_data
    print_data = str(numpy_mat)


def file_input(file_path):
    # file = open('../../test_data/Gauss_Input.txt')
    # file = open('../test.txt')
    file = open(file_path)
    file_content = file.readlines()
    for idx, line in enumerate(file_content):
        if idx == 0:
            global N
            N = int(line.strip().split()[0])
        else:
            mat.append(list(map(int, line.strip().split()))[:])

    file.close()


def file_output(file_path):
    file = open(file_path, 'w')
    file.writelines(print_data)
    file.close()


def pivoting():
    mat.sort(key=lambda row: tuple([elem for elem in row]), reverse=True)


def get_echelon_form():
    for i in range(N - 1):
        기준행 = mat[i]
        col = i
        for j in range(i + 1, N):
            대상행 = mat[j]
            A = 기준행[col]
            B = 대상행[col]
            임시행 = [deepcopy(v * -(B / A)) for v in 기준행]
            대상행 = [deepcopy(대상행[i] + 임시행[i]) for i in range(N + 1)]
            mat[j] = deepcopy(대상행)


def get_result():
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            mat[i][N] = mat[i][N] - mat[i][j] * mat[j][N]
        mat[i][N] /= mat[i][i]


def print_result():
    global print_data
    for i in range(N):
        print_data += f'\nx{i} = {mat[i][N]}'
        # print(f'x{i} = {mat[i][N]}')


def run():
    pivoting()
    get_echelon_form()
    print_matrix()
    get_result()
    print_result()
    return print_data

# def main():
#     file_input()
#     run()
#
#
# if __name__ == '__main__':
#     main()

# file_input(None)
# run()
