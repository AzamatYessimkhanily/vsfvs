
def smallestInRow(mat, n, m):
    print("{", end="")
    for i in range(n):

        min = mat[i][0]

        for j in range(1, m, 1):

            if (mat[i][j] < min):
                min = mat[i][j]

        print(min, end=",")

    print("}")


def smallestInCol(mat, n, m):
    print("{", end="")
    for i in range(m):

        min = mat[0][i]

        for j in range(1, n, 1):

            if mat[j][i] < min:
                min = mat[j][i]

        print(min, end=",")

    print("}")


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print("Minimum element of each row is",
      end=" ")
smallestInRow(a, n, m)

print("Minimum element of each column is",
      end=" ")
smallestInCol(a, n, m)
