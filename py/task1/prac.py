import math
a=str(input("^ ,[ , o:"))
if a=='o':
    r=int(input("That is  radius:"))
    print("area is:"," ",math.pi*pow(r,2))
elif a=='[':
    first=int(input("That is  1st side:"))   
    second=int(input("That is  2th side:"))
    print("area is:"," ",first*second)
elif a=="^":
    side1=int(input("That is  1st side:"))   
    side2=int(input("That is  2th side:"))
    side3=int(input("That is  3th side:"))
    p=(side1+side2+side3)/2
    s=math.sqrt(p*(p-side1)*(p-side2)*(p-side3))
    print("area is:",s)
