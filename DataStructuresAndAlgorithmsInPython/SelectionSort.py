
def selectIndexOfMinimum(array, p, r):
    minimumIndex = p
    i = p
    while i <= r:
        if array[minimumIndex] > array[i]:
            minimumIndex = i
        i = i + 1
    return minimumIndex

array = [3,5,1,2,4,-1]
assert(selectIndexOfMinimum(array, 0, len(array) - 1) is 5)


def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

array = [3,5,1,2,4]
swap(array, 0, 1)
assert(array == [5,3,1,2,4])


def selectionSort(array, p, r):
    if p < r:
        i = selectIndexOfMinimum(array, p, r)
        swap(array, p, i)
        selectionSort(array, p+1, r)

array = [3,5,1,2,4]
selectionSort(array, 0, 4)
assert(array == [1,2,3,4,5])