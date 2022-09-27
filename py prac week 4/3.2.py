n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('orifin array: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

max = a[0][0]
ie = je = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > max:
            max = a[i][j]
            ie = i
            je = j
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))
