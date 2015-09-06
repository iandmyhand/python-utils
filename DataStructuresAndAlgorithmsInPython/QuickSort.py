def swap(arr, firstIndex, secondIndex):
	temp = arr[firstIndex]
	arr[firstIndex] = arr[secondIndex]
	arr[secondIndex] = temp

arr = [-3,5,0,1,3]
swap(arr, 0, 1)
assert arr == [5,-3,0,1,3]


def partition(arr, p, r):
	b = p
	i = p
	while i < r:
		# 1,4,2,5,0 | i:0, r:4, b:0
		# 1,4,2,5,0 | i:1, r:4, b:1
		# 1,4,2,5,0 | i:2, r:4, b:1
		# 1,2,4,5,0 | i:3, r:4, b:2
		# 1,2,4,5,0 | i:4, r:4, b:2
		if arr[i] <= arr[r]:
			swap(arr, b, i)
			b = b + 1
		i = i + 1
	swap(arr, b, r)
	return b

arr = [-3,5,0,1,3]
pivot = partition(arr, 0, len(arr) - 1) # -3, 0, 1, 3, 5
assert pivot is 3


def quickSort(arr, p, r):
	i = 0 
	while i < (r - p):
		pivot = partition(arr, p, r)
		quickSort(arr, p, pivot - 1)
		quickSort(arr, pivot + 1, r)
		i = i + 1

arr = [-3,5,0,1,3]
quickSort(arr, 0, 4)
assert arr == [-3,0,1,3,5]