n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])

a_rev = list(map(list, zip(*a)))
for i in range(n):
    for j in range(n):
        if a[i] == a_rev[j]:
            print(i + 1, 'row and', j + 1, 'column are equal')
