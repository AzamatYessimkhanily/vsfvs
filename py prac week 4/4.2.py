n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('origib array:')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

a = [[1 if x > 0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))], '')
