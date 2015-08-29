import math

def binarySearch(array, targetValue):
    minimum = 0;
    maximum = len(array) - 1
    guess = -1

    while maximum >= minimum:
        guess = int(math.floor((minimum + maximum) / 2))
        # maximum: 4 4 4 4
        # minimum: 0 3 4 5
        # guess: 2 3 4 return -1
        if array[guess] == targetValue:
            return guess
        elif array[guess] < targetValue:
            minimum = guess + 1
        else:
            maximum = guess - 1

    return -1;

sampleArray = [1,2,3,4,5]
assert(binarySearch(sampleArray, 6) == -1)
assert(binarySearch(sampleArray, 1) == 0)
assert(binarySearch(sampleArray, 5) == 4)