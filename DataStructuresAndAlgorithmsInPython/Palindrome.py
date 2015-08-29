def firstCharacter(str):
    return str[:1]

assert(firstCharacter("abc") is "a")


def lastCharacter(str):
    return str[-1:]

assert(lastCharacter("abc") is "c")


def middleCharacters(str):
    return str[1:-1]

assert(middleCharacters("abc") == "b")
assert(middleCharacters("abcde") == "bcd")


def isPalindrome(str):
    if len(str) <= 1:
        return True
    if firstCharacter(str) != lastCharacter(str):
        return False
    return isPalindrome(middleCharacters(str))

assert(isPalindrome("a") == True)
assert(isPalindrome("taste") == False)
assert(isPalindrome("roror") == True)
