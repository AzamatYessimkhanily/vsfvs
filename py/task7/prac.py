import math


def quadrilateralArea(lst):
    s = (lst[0] + lst[1] + lst[2] + lst[3]) / 2
    area = math.sqrt(((s - lst[0]) * (s - lst[1]) * (s - lst[2]) * (s - lst[3])) - (
                lst[0] * lst[1] * lst[2] * lst[3] * math.pow(math.cos(math.pi / 2), 2)))
    return area


x = list(map(int, input("enter 4 sides one after one: ").split()))
print("area of quadrilateral: ", quadrilateralArea(x))
