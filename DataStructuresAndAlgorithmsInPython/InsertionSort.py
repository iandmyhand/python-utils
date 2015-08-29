def insert(array, rightIndex, value):
    index = rightIndex
    while index >= 0 and array[index] > value:
        # index: 0 -1
        array[index + 1] = array[index]
        index = index - 1
    array[index + 1] = value

sampleArray = [5, 1, -3]
insert(sampleArray, 0, 1)
assert(sampleArray == [1, 5, -3])
insert(sampleArray, 1, -3)
assert(sampleArray == [-3, 1, 5])

def insertionSort(array):
    index = 1
    while index < len(array):
        # index: 1 2 3 4 5 6
        insert(array, index - 1, array[index])
        index = index + 1

sampleArray = [5, 1, -3, 0, 22, 13]
insertionSort(sampleArray)
assert(sampleArray == [-3, 0, 1, 5, 13, 22])
sampleArray = [66, 21, -144, 0, 5]
insertionSort(sampleArray)
assert(sampleArray == [-144, 0, 5, 21, 66])