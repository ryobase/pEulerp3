""" Problem 21:
Evaluate the sum of all the amicable numbers under 10000 """

import common

def sumOfDivisors(x):
    s = 1
    for i in range(2, common.root(x)+1, 1):
        if (x % i == 0):
            s+=i
            if (x//i != i): # For handling perfect squares
                s+=x//i
    return s

def isAmicable(a):
    b = sumOfDivisors(a)
    return a != b and sumOfDivisors(b) == a

def main():
    s = 0
    for i in range(1, 10000):
        if (isAmicable(i)):
            print(i)
            s+=i
    print(s)

if __name__ == '__main__':
    main()