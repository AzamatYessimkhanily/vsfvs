x = int(input("enter the x: "))
m = int(input("enter the y: "))
a = []
for i in range(x):
    a.append(list(map(int, input().split())))
p = 0
s = 0
for i in range(x):
    for j in range(i + 1, x):
        if a[i][j] > 0:
            s += a[i][j]
            p+= 1

print("number of positive:",p)
print("sum:",s)
