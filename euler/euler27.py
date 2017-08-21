""" Problem 27:
Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with  n=0. """

import common, itertools

def main():
    p = common.primeList(1000)
    
    def isPrime(n):
        if n < 0:
            return False
        elif n < len(p):
            return p[n]
        return common.isPrime(n)

    n_max = a_max = b_max = 0
    for a in range(-1000, 1000, 1):
        for b in range(1, 1000, 1):
            n = 0
            for i in itertools.count():
                if not isPrime(i * i + a * i + b):
                    n = i
                    break
            if n > n_max:
                n_max = n
                a_max = a
                b_max = b
    print(a_max * b_max)

if __name__ == '__main__':
    main()