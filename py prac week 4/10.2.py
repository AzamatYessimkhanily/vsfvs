def sortRowWise(m):
    for i in range(len(m)):

        for j in range(len(m[i])):

            for k in range(len(m[i]) - j - 1):

                if m[i][k] > m[i][k + 1]:
                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))
sortRowWise(a)
