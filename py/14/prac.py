
from math import *

def countDivisors(n) :
	count = 0
	

	for i in range(1,int(sqrt(n)+1)) :
		if n % i == 0 :

			if n / i == i :
				count += 1
				

			else :
				count += 2

	return count


def MaximumDivisors(X,Y) :
	result = 0
	maxDivisors = 0


	arr = []
	
	for i in range(Y - X + 1) :
		arr.append(0)

	for i in range(X,Y+1) :


		Div = countDivisors(i)


		arr[i - X] = Div
		

		maxDivisors = max(Div,maxDivisors)
		

	for i in range (Y - X + 1) :


		if arr[i] == maxDivisors :
			result += 1

	return result

if __name__ == "__main__" :

	X, Y = 1, 10


	print(MaximumDivisors(X,Y))
