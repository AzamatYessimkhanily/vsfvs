x = int(input("enter the x: "))
y = int(input("enter the y: "))
a = []
print("enter the row by row")
for i in range(x):
    a.append(list(map(int, input().split())))

print('origin array: ')
for i in range(y):
    for j in range(x):
        print(a[i][j], end=' ')
    print()
for i in range(x):
    tmp = a[i][0]
    a[i][0] = a[i][y-1]
    a[i][y-1] = tmp

for i in range(x):
    for j in range(y):
        print("%2d " % a[i][j], end=' ')
    print()
