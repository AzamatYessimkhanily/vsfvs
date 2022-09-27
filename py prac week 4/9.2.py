def getcofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def determinantOfMatrix(mat):
    if len(mat) == 2:
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value

    Sum = 0

    for current_column in range(len(mat)):
        sign = (-1) ** current_column

        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))

        Sum += (sign * mat[0][current_column] * sub_det)

    return Sum


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))
print('Determinant of the matrix is :', determinantOfMatrix(a))
