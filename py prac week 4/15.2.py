import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i] - b[i]), 2)
    return d
Identify = ['X', 'Y', 'Z', 'T']
arr = []
print("enter the coordinates:")
for i in range(4):
    b = []
    print("coordinates:", Identify[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
flag = True
for i in range(3):
    for j in range(i + 1, 4):
        dist = distance(arr[i], arr[j])
        if flag or min_dist > dist:
            m1 = i
            m2 = j
            min_dist = dist
            flag = False
print(f'minimal distance from each other: {Identify[m1]} и {Identify[m2]}')
print(f'value of this distance:  {min_dist ** 0.5:.3f}')