def swap(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
    return lst
input("the length of array: ")
list_new = list(map(int, (input("Enter the array: ")).split()))
print("original array: ",list_new)
print("swapped: ",swap(list_new))