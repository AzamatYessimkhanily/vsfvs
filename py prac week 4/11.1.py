n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])

min_ = [min(i) for i in a]
ind_row_with_min = min_.index(min(min_))

print('Min of array: ', min(map(min, a)))
print('Sum: ', format(sum(a[ind_row_with_min])))
