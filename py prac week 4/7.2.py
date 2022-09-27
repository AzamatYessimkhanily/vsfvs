def diagonal(A, n, m):
    for col in range(m):

        startcol = col
        startrow = 0

        while (startcol >= 0 and
               startrow < m):
            print(A[startrow][startcol], end=" ")

            startcol -= 1
            startrow += 1

        print()

    for row in range(1, n):
        startrow = row
        startcol = n - 1

        while (startrow < n and
               startcol >= 0):
            print(A[startrow][startcol],
                  end=" ")

            startcol -= 1
            startrow += 1

        print()


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

diagonal(a, n, m)
