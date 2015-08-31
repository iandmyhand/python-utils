import math

def merge(array, p, q, r):
	lowHalf = array[p:q+1]
	highHalf = array[q+1:r+1]
	l = 0
	h = 0
	i = p
	while l < len(lowHalf) and h < len(highHalf):
		if lowHalf[l] <= highHalf[h]:
			array[i] = lowHalf[l]
			l = l + 1
		else:
			array[i] = highHalf[h]
			h = h + 1
		i = i + 1
	while l < len(lowHalf):
		array[i] = lowHalf[l]
		l = l + 1
		i = i + 1
	while h < len(highHalf):
		array[i] = highHalf[h]
		h = h + 1
		i = i + 1

array = [1,5,6,7,-1,0,1]
merge(array, 0, int(math.floor((0 + (len(array) - 1)) / 2)), len(array) - 1)
assert(array == [-1, 0, 1, 1, 5, 6, 7])

def mergeSort(array, p, r):
	if p < r:
		q = int(math.floor((p + r) / 2))
		mergeSort(array, p, q)
		mergeSort(array, q+1, r)
		merge(array, p, q, r)

array = [3, -1, 0, 12, 55]
mergeSort(array, 0, len(array) - 1)
assert(array == [-1, 0, 3, 12, 55])