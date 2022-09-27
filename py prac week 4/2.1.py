x = int(input("enter the x: "))
y = int(input("enter the y: "))
a = []
print("enter the row by row")
for i in range(x):
    a.append(list(map(int, input().split())))


def magSquare(a):
    diag1 = 0
    diag2 = 0
    for i in range(x):
        diag1 += a[i][i]
        diag2 += a[i][x - i - 1]
    if not (diag1 == diag2):
        return False
    for i in range(x):
        rows = 0
        cols = 0
        for j in range(x):
            rows += a[i][j]
            cols += a[j][i]
        if not (rows == cols == diag1):
            return False

    return True


if (magSquare(a)):
    print("Magic Square")
else:
    print("Not a magic Square")
