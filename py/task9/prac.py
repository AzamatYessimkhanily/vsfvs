def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


def sumComb(n, sum):
    repeat = -1
    while n >= 0:
        n -= sum
        repeat += 1
    return repeat


n = int(input("enter the number: "))
sum = getSum(n)
print(sum)
print(sumComb(n, sum))