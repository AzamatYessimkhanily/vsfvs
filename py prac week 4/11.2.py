from operator import mul
from functools import reduce


def mprint(matrix):
    for row in matrix:
        for item in row:
            print(f'{item:>3}', end=' ')
        print()


n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])

tmatrix = list(zip(*a))
ps = [reduce(mul, row) for row in tmatrix]
min_p = min(ps)
idx = ps.index(min_p)

if idx < n - 1:
    tmatrix[idx], tmatrix[idx + 1] = tmatrix[idx + 1], tmatrix[idx]
else:
    tmatrix[idx], tmatrix[idx - 1] = tmatrix[idx - 1], tmatrix[idx]

matrix = list(zip(*tmatrix))
mprint(matrix)
