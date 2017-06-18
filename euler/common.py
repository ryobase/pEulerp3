""" This module provide common functions that are used quite frequently."""

import math

# Test to see whether the input is a prime number or not
# https://en.wikipedia.org/wiki/Primality_test
def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0:
        return False
    else:
        m = math.floor(math.sqrt(n))
        for i in range(3, m + 1, 2):
            if n%i == 0:
                return False
        return True

# Greatest common divisor for all natural numbers
# https://en.wikipedia.org/wiki/Greatest_common_divisor
def gcd(a, b):
    if a <= 0:
        return 0
    elif b == 0:
        return a
    return gcd(b, a%b)

# Check to see if an input is a Palindrome number
def isPalindrome(n):
    rev = 0
    num = n
    while num > 0:
        rev = (rev * 10) + (num % 10)
        # Due to dynamic typing nature of Python floor division is needed
        num = num//10
    return rev == n

# Check to see whether an input is even number
def isEven(n):
    return n%2 == 0

# Check to see if an input is a perfect root (natural number)
def isPerfectRoot(n):
    if n < 0:
        return False
    m = math.sqrt(abs(n))
    return math.pow(m, 2) == n