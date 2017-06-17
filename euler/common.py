""" This module provide common functions that are used quite frequently."""

import math

# Test prime number
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