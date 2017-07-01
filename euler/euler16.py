""" Problem 16:
Find the sum of digits of 2^1000 """

import math

# This problem is very trival for modern programming language like Python since it can handle
# very large number by default
def powSquare(n):
    return str(int(math.pow(2, n)))

def main():
    x = powSquare(1000)
    s = 0
    for i in range(len(x)):
        s += int(x[i])
    print("{}".format(s))

if __name__ == '__main__':
    main()