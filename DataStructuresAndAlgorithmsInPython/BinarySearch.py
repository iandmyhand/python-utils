##-*- coding: utf-8 -*- 
#!/usr/bin/python
""" Returns either the index of the location in the array,
    or -1 if the array did not contain the targetValue
"""
import math


def binarySearch (array, targetValue):
    minimum = 0;
    maximum = len(array) - 1;
    guess = -1;
    guessesCount = 0;
    
    while (maximum >= minimum):
        guessesCount += 1;
        guess = int(math.floor((minimum + maximum) / 2));
        print "A number of guess: " + str(guess);
        
        if (array[guess] == targetValue):
            print "Total number of guesses: " + str(guessesCount);
            return guess;   
        elif (array[guess] < targetValue):
            minimum = guess + 1;
        else:
            maximum = guess - 1;

    return -1;

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

result = binarySearch(primes, 73);
print "Found prime at index " + str(result);

assert (binarySearch(primes, 7) is 3)
assert (binarySearch(primes, 13) is 5)
assert (binarySearch(primes, 73) is 20)