def AreaOfTriangle():
    a=int(input("Firts catet:"))
    b=int(input("Second catet:"))
    c=(a*b)/2
    if a>b:
        print("First catet if bigger than second and are is:",c)
    elif a<b:
         print("second  catet if bigger than First and are is:",c)

AreaOfTriangle()