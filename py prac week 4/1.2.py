x = int(input("enter the x: "))
m = int(input("enter the y: "))
a = []
for i in range(x):
    a.append(list(map(int, input().split())))
def min_elts(a):
    return list(map(min,a))
