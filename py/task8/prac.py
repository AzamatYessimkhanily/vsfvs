def divisible(n):
    for i in range(n):
        if allDigitsDivide(i) == True:
            print(i)


def allDigitsDivide(n):
    temp = n
    while (temp > 0):

        digit = temp % 10
        if ((digit != 0 and n % digit == 0) == False):
            return False

        temp = temp // 10

    return True


n = int(input("enter the numb: "))
divisible(n)