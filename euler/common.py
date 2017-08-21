""" This module provide common functions that are used quite frequently."""

import math

# Floor square root
def root(n):
    return math.floor(math.sqrt(n))

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

# Generate a list of prime numbers using Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def primeList(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(root(n) + 1):
        if p[i] is True:
            for j in range(i * i, len(p), i):
                p[j] = False
    return p

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
def isOdd(n):
    return n & 1 and True or False

# Check to see if an input is a perfect root (natural number)
def isPerfectRoot(n):
    if n < 0:
        return False
    m = math.sqrt(abs(n))
    return math.pow(m, 2) == n

# Fast Fibonacci sequence calculation
# https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
def fibs(n):
    if n < 0:
        raise ValueError("Negative number is not allow")
    def _f(_n):
        if _n == 0:
            return [0, 1]
        else:
            # a = Fn and b = Fn+1
            a, b = _f(_n // 2)
            # Subtraction because we're using Fn+1 instead of Fn-1
            c = a * (b * 2 - a)
            d = a * a + b * b
            if isOdd(_n):
                return (d, c + d)
            else:
                return (c, d)
    return _f(n) [0] # return Fn


