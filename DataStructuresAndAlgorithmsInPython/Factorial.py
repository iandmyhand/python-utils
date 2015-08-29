
def factorial(n):
    if n is 0:
        return 1
    return n * factorial(n-1)

assert(factorial(5) == 120)
assert(factorial(3) == 6)