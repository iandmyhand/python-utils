def isOdd(n):
    return n % 2 == 1

assert(isOdd(1) == True)
assert(isOdd(2) == False)

def isEven(n):
    return not isOdd(n)

assert(isEven(1) == False)
assert(isEven(2) == True)

def power(x, n):
    if n is 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if isOdd(n):
        return x * power(x, n-1)
    if isEven(n):
        y = power(x, n/2)
        return y * y

assert(power(3, 0) == 1)
assert(power(3, 1) == 3)
assert(power(3, 2) == 9)
assert(power(3, -1) == 1/3)