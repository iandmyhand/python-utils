def selectIndexOfMinimum(array, startIndex):
    minimumIndex = startIndex
    minimumValue = array[startIndex]
    index = startIndex
    while index < len(array):
        if(array[index] < minimumValue):
            minimumIndex = index
            minimumValue = array[index]
        index = index + 1
    return minimumIndex

sampleArray = [2,4,1,3,5]
assert(selectIndexOfMinimum(sampleArray, 0) == 2)
assert(selectIndexOfMinimum(sampleArray, 2) == 2)
assert(selectIndexOfMinimum(sampleArray, 3) == 3)

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp
    return array

sampleArray = [1,2,3,4,5]
assert(swap(sampleArray, 0, 1) == [2,1,3,4,5])
assert(swap(sampleArray, 3, 1) == [2,4,3,1,5])

def selectionSort(array):
    index = 0
    for value in array:
        indexOfMin = selectIndexOfMinimum(array, index)
        swap(array, index, indexOfMin)
        index = index + 1
    return array

sampleArray = [2,4,1,3,5]
assert(selectionSort(sampleArray) == [1,2,3,4,5])
assert(selectionSort(sampleArray) == [1,2,3,4,5])
sampleArray = [99,42,1,32,5]
assert(selectionSort(sampleArray) == [1,5,32,42,99])