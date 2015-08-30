def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

sampleArray = [-5, 80, 0, 12, 3]
swap(sampleArray, 0, 1)
assert(sampleArray == [80, -5, 0, 12, 3])


def partition(array, p, r):
    q = p
    j = p
    while j < r:
        if array[j] <= array[r]:
            swap(array, j, q)
            q = q + 1
        j = j + 1
    swap(array, q, r)
    return q

sampleArray = [-5, 80, 0, 12, 3]
pivot = partition(sampleArray, 0, len(sampleArray) - 1)
assert(pivot is 2)
assert(sampleArray == [-5, 0, 3, 12, 80])


def quickSort(array, p, r):
    if p < r:
        pivot = partition(array, p, r)
        quickSort(array, p, pivot-1)
        quickSort(array, pivot+1, r)

sampleArray = [-5, 80, 0, 12, 3]
quickSort(sampleArray, 0, len(sampleArray) - 1)
assert(sampleArray == [-5, 0, 3, 12, 80])