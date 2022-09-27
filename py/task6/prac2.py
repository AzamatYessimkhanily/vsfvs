import math


def quadrilateralArea(lst, diagonal):
    h1 = 2 * (areaTriangle(lst[0], lst[1], diagonal) / diagonal)
    h2 = 2 * (areaTriangle(lst[2], lst[3], diagonal) / diagonal)
    area = 0.5 * diagonal * (h1 + h2)
    return area


def areaTriangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


x = list(map(float, input("enter 4 sides one after one: ").split()))
d = float(input("enter the diagonal: "))
print("area of quadrilateral: ", quadrilateralArea(x, d))