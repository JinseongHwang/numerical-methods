from typing import Final

MAT_SIZE: Final = 3

mat = []


def file_input():
    f = open('../test_data/diagonally_dominant_data.txt')
    lines = f.readlines()
    for line in lines:
        mat.append(list(map(int, line.strip().split())))


def validation():
    for row in range(MAT_SIZE):
        sum = 0

        for col in range(MAT_SIZE):
            if row == col:
                continue
            sum += abs(mat[row][col])

        if abs(mat[row][row]) < sum:
            return False

    return True


def main():
    file_input()
    if validation():
        print('대각 우세 행렬입니다.')
    else:
        print('대각 우세 행렬이 아닙니다.')


if __name__ == '__main__':
    main()
