numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
numbers2=[1,2,3,4,5,6,7]
numbers3=[1,2,5,6,7,8]
sum = 0
a=0
b=0
for i in numbers:
    sum = sum+i
print("The sum if first arr", sum) 
print("The arithmetic mean of first",sum/len(numbers))
for k in numbers2:
    a = a+k
print("The sum if second arr", a)
print("The arithmetic mean of second",a/len(numbers2))
for j in numbers3:
    b = b+j
print("The sum if third arr", b)
print("The arithmetic mean of third",b/len(numbers3))

