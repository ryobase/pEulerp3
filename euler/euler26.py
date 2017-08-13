""" Problem 26:
ind the value of d < 1000 for which 1/d
contains the longest recurring cycle in its decimal fraction part. """

import itertools

def main():
    l = 0
    m = 0
    for i in range(1, 1000, 1):
        arr = {}
        x = 1
        pos = 0
        while (x not in arr):
            arr[x] = pos
            x = x * 10 % i
            pos += 1
        if (pos - arr[x]) > l:
            l = pos - arr[x]
            m = i
    print("Number with the longest recurring cycle is {0}".format(m))

if __name__ == '__main__':
    main()