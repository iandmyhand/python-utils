import math
import copy



def binarySearch(array, target):
    minimum = 0
    maximum = len(array) - 1
    guess = -1

    while (maximum >= minimum):
        # print 'maximum: ' + str(maximum) # 4 4 4 4
        # print 'minimum: ' + str(minimum) # 0 3 4 5

        guess = int(math.floor((maximum + minimum) / 2)) # 2 3 4
        if (array[guess] == target):
            return guess
        elif (array[guess] < target):
            minimum = guess + 1
        else:
            maximum = guess - 1

    return -1

primes = [2,3,4,5,6]
assert(binarySearch(primes, 7) == -1)
assert(binarySearch(primes, 2) == 0)
assert(binarySearch(primes, 6) == 4)



def indexOfMinimum(array, startIndex):
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
assert(indexOfMinimum(sampleArray, 0) == 2)
assert(indexOfMinimum(sampleArray, 2) == 2)
assert(indexOfMinimum(sampleArray, 3) == 3)

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
        indexOfMin = indexOfMinimum(array, index)
        swap(array, index, indexOfMin)
        index = index + 1
    return array

sampleArray = [2,4,1,3,5]
assert(selectionSort(sampleArray) == [1,2,3,4,5])
assert(selectionSort(sampleArray) == [1,2,3,4,5])
sampleArray = [99,42,1,32,5]
assert(selectionSort(sampleArray) == [1,5,32,42,99])