import math

def merge(array, p, q, r):
    lowHalf = []
    highHalf = []
    i = 0
    j = 0
    k = p
    while i <= (q - p): # i <= 2
        lowHalf.append(array[k])
        i = i + 1
        k = k + 1
    while j <= (r - (q+1)): # j <= 2
        highHalf.append(array[k])
        j = j + 1
        k = k + 1

    i = 0
    j = 0
    k = p
    while i < len(lowHalf) and j < len(highHalf):
        if lowHalf[i] < highHalf[j]:
            array[k] = lowHalf[i]
            i = i + 1
        else:
            array[k] = highHalf[j]
            j = j + 1
        k = k + 1
    while i < len(lowHalf):
        array[k] = lowHalf[i]
        i = i + 1
        k = k + 1
    while j < len(highHalf):
        array[k] = highHalf[j]
        j = j + 1
        k = k + 1

sampleArray = [-3, 0, 1, -99, -32, 81]
merge(sampleArray, 0, int(math.floor((0 + len(sampleArray)-1) / 2)), len(sampleArray)-1) # merge(a, 0, 2, 5)
assert(sampleArray == [-99, -32, -3, 0, 1, 81])

def mergeSort(array, p, r):
    if(p < r):
        q = int(math.floor((p + r) / 2))
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)

sampleArray = [0, -32, 1, -99, 81, -3, 5]
mergeSort(sampleArray, 0, len(sampleArray)-1)
assert(sampleArray == [-99, -32, -3, 0, 1, 5, 81])