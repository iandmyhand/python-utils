import math

def binarySearch(array, target):
    minimum = 0
    maximum = len(array) - 1
    guess = -1

    while (maximum >= minimum):
        print 'maximum: ' + str(maximum) # 4 4 4 4
        print 'minimum: ' + str(minimum) # 0 3 4 5

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