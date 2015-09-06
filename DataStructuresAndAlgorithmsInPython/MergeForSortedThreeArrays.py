#!/usr/bin/python
# -*- coding: utf-8 -*-

def mergeForSortedTwoArrays(arr, n, arr1, i, arr2, j):
    while i >= 0 and j >= 0:
        if arr1[i] >= arr2[j]:
            arr[n] = arr1[i]
            i = i - 1
        else:
            arr[n] = arr2[j]
            j = j - 1
        n = n - 1

    while i >= 0:
        arr[n] = arr1[i]
        i = i - 1
        n = n - 1
    while j >= 0:
        arr[n] = arr2[j]
        j = j - 1
        n = n - 1

def mergeForSortedThreeArrays(bigArr, arr2, arr3):
    n = len(bigArr) - 1
    i = len(bigArr) - 1
    j = len(arr2) - 1
    k = len(arr3) - 1

    while i >= 0:
        if not bigArr[i]:
            i = i - 1
        else:
            break

    while i >= 0  and j >= 0  and k >= 0 :
        if bigArr[i] >= arr2[j] and bigArr[i] >= arr3[k]:
            bigArr[n] = bigArr[i]
            i = i - 1
        elif arr2[j] >= bigArr[i] and arr2[j] >= arr3[k]:
            bigArr[n] = arr2[j]
            j = j - 1
        else:
            bigArr[n] = arr3[k]
            k = k - 1
        n = n - 1

    if i is -1:
        mergeForSortedTwoArrays(bigArr, n, arr2, j, arr3, k)
    elif j is -1:
        mergeForSortedTwoArrays(bigArr, n, bigArr, i, arr3, k)
    elif k is -1:
        mergeForSortedTwoArrays(bigArr, n, bigArr, i, arr2, j)

arr1 = [-3,0,12,15,20, None, None, None, None, None]
arr2 = [1,3]
arr3 = [2,6,9]
mergeForSortedThreeArrays(arr1, arr2, arr3)
assert(arr1 == [-3, 0, 1, 2, 3, 6, 9, 12, 15, 20])