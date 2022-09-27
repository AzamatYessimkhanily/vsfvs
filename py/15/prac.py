
INT_MAX = 2147483647




def isKthBitSet(x, k):

	return 1 if (x & (1 << (k - 1))) else 0



def leftmostSetBit(x):

	count = 0
	while (x):
		count += 1
		x = x >> 1

	return count


def isBinPalindrome(x):

	l = leftmostSetBit(x)
	r = 1


	while (l > r):


		if (isKthBitSet(x, l) != isKthBitSet(x, r)):
			return 0
		l -= 1
		r += 1
	return 1


def findNthPalindrome(n):
	pal_count = 0

	i = 0
	for i in range(1, INT_MAX + 1):
		if (isBinPalindrome(i)):
			pal_count += 1


		if (pal_count == n):
			break

	return i



if __name__ == "__main__":
	n = 9

	print(findNthPalindrome(n))

