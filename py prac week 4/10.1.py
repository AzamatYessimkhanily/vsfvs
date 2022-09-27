def maxElement(arr):
    numb_of_rows = len(arr)
    numb_of_column = len(arr[0])

    for i in range(numb_of_rows):

        max1 = 0
        for j in range(numb_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]

        print("max element in row",max1)


n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

maxElement(a)
