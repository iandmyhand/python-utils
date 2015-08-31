import math

def binarySearch(array, target):
	minimum = 0
	maximum = len(array) - 1
	guess = -1
	while minimum <= maximum:
		guess = int(math.floor((minimum + maximum) / 2))
		if array[guess] is target:
			return guess
		elif array[guess] < target:
			minimum = guess + 1
		else:
			maximum = guess - 1
	return -1

array = [1,2,3,4,5]
assert(binarySearch(array, 6) == -1)
assert(binarySearch(array, 1) == 0)
assert(binarySearch(array, 4) == 3)