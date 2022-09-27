import math


def isInside(x, y, radius):
    if math.pow(x, 2) + math.pow(y, 2) <= pow(radius, 2):
        return True


R = input("plz input R of circle: ")
wannaExit = False
while(wannaExit!=True):
    x, y = list(map(int, input("enter x,y of point").split()))
    wannaExit = bool(input("wanna quit?"))
    isInside(x, y, R)
