""" Problem 20:
Find the sum of the digits in the number 100! """

import math

# This problem is trival for modern programming language like Python
def fact(x):
    f = math.factorial(x)
    return str(f)

def main():
    arr = fact(100)
    s = 0
    for i in range(len(arr)):
        s+=int(arr[i])
    print("{}".format(s))

if __name__ == '__main__':
    main()