def printArray(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def sortArr(arr, m, n):
    for i in range(m):
        arr[i].sort()
    print()


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('origin array: ')
printArray(a, m, n)

sortArr(a, m, n)
print('changed array:')
printArray(a, m, n)
