import statistics

def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result


list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for i in range(3):
    print("The product of the elements in",i+1," list =", multiplyList(list[i]))

for i in range(3):
    print("The arithmetic mean of ",i+1,"list =", statistics.mean(list[i]))