""" Problem 25:
Find the index of the first Fibonacci sequence term to contain 1000 digits """

import common

def main():
    # I've calculated the index beforehand to guess the appropriate starting range
    # Index of less than 1000 does not meet the sufficient length
    index = 4000
    while True:
        res = common.fibs(index)
        if len(str(res)) is 1000:
            break
        index+=1
    print("{}".format(index))

if __name__ == '__main__':
    main()