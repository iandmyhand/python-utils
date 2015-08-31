
def swap(array, firstIndex, secondIndex):
	temp = array[firstIndex]
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = temp
array = [-3,0,-21,88,2]
swap(array, 0, 1)
assert(array == [0,-3,-21,88,2])

def partition(array, p, r):
	pivot = p
	i = p
	while i < r:
		if array[i] < array[r]:
			swap(array, pivot, i)
			pivot = pivot + 1
		i = i + 1
	swap(array, pivot, r)
	return pivot

array = [-3,5,0,88,2]
pivot = partition(array,0,len(array)-1)
assert(pivot is 2)
assert(array == [-3,0,2,88,5])
# -3,5,0,88,2
# -3,0,5,88,2
# -3,0,2,88,5

def quickSort(array, p, r):
	if p < r:
		pivot = partition(array, p, r)
		quickSort(array, p, pivot-1)
		quickSort(array, pivot+1, r)

array = [-3,0,-21,88,2]
quickSort(array, 0, len(array)-1)
assert(array == [-21,-3,0,2,88])