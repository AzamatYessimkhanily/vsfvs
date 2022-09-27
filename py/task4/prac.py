import math


def divide(lst):
    list_new1 = list(map(int, arr[0].split('/')))
    list_new2 = list(map(int, arr[1].split('/')))
    return reduceF([list_new1[0] * list_new2[1], list_new1[1] * list_new2[0]])


def reduceF(lst):
    divider, x, y = gcdEuclid(lst[0], lst[1])
    return [i / divider for i in lst]


def gcdEuclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdEuclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


arr = []
for i in range(2):
    arr.append(input("enter the fraction n" + str(i + 1) + ": "))
result = divide(arr)
print(result[0], "/", result[1])