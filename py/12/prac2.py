import math


def median(a, b, c):
    median = math.sqrt(2 * (b * b + c * c) - a * a) / 2
    return median


print("enter 3 sides:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if abs(a - b) >= c | a + b <= c:
    print("impossible triangle")
print("medians of original triangle:")
ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)
print(ma, mb, mc)
print("medians of created triangle:")
mma = median(ma, mb, mc)
mmb = median(mb, ma, mc)
mmc = median(mc, ma, mb)
print(mma, mmb, mmc)