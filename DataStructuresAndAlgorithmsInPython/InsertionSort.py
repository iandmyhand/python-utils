def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

array = [-3,1,22,0,2]
swap(array, 0, 1)
assert(array == [1,-3,22,0,2])


def insert(array, target):
    i = target - 1
    targetValue = array[target]
    while i >= 0:
        if array[i] > targetValue:
            swap(array, i, i + 1)
        else:
            return
        i = i - 1

array = [-3,1,22,0,2]
insert(array, 3)
assert(array == [-3,0,1,22,2])


def insertionSort(array, p, r):
    i = p
    while i <= r:
        insert(array, i)
        i = i + 1

array = [-3,1,22,0,2]
insertionSort(array, 0, 4)
assert(array == [-3,0,1,2,22])