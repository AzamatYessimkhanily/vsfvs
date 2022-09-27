def diagonalsMinMax(mat):
    n = len(mat)
    if n == 0:
        return

    principalMin = mat[0][0]
    principalMax = mat[0][0]
    secondaryMin = mat[0][n - 1]
    secondaryMax = mat[0][n - 1]

    for i in range(1, n):

        for j in range(1, n):

            if i == j:

                if mat[i][j] < principalMin:
                    principalMin = mat[i][j]

                if mat[i][j] > principalMax:
                    principalMax = mat[i][j]

            if (i + j) == (n - 1):

                if mat[i][j] < secondaryMin:
                    secondaryMin = mat[i][j]

                if mat[i][j] > secondaryMax:
                    secondaryMax = mat[i][j]

    print("Principal Diagonal Smallest Element: ",
          principalMin)
    print("Principal Diagonal Greatest Element : ",
          principalMax)

    print("Secondary Diagonal Smallest Element: ",
          secondaryMin)
    print("Secondary Diagonal Greatest Element: ",
          secondaryMax)


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))
diagonalsMinMax(a)
