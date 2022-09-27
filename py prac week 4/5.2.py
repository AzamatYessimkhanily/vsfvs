def smallestInRow(mat):
    minm = min(mat)
    return minm


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('origin array: ')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
minm = []
for i in range(n):
    minm.append(smallestInRow(a[i]))
print(minm)

for i in range(len(minm)):
        if minm[i]%2==0:
            minm[i]=0
        else:
            minm[i]=1
print(minm)
