def findMax(lst):
    return max(lst)


arr = input("Enter the array: ")
list1 = list(map(int, arr.split()))
print("maximum of 1st list:", findMax(list1))

arr = input("Enter the array: ")
list2 = list(map(int, arr.split()))
print("maximum of 2nd list:", findMax(list2))

index1 = list1.index(findMax(list1))
index2 = list2.index(findMax(list2))

list1[index1], list2[index2] = list2[index2], list1[index1]

print(list1, list2)