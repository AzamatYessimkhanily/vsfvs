n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('origin array: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
b = "YES"
for i in range(m):
    for j in range(n):
        if a[i][j] != a[j][i]:
            b = "NO"
            break
print(b)
