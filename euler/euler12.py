""" Problem 12:
Find the value of the first triangle number to have over five hundred divisors """

import common

# This formula is not really necessary since we have to try every possible numbers anyway
def trigNum(n):
    return (n*(n+1))//2

def run(lim):
    _lim = lim-1
    candidate = 0
    i = 1
    n = 1
    s = False
    while not s:
        count = 0
        candidate = trigNum(i)
        i+=1

        # Second attempt is much faster
        n = common.root(candidate)
        for j in range(1, n+1):
            if candidate%j == 0:
                count+=2
        if n**2 == candidate:
            count-=1
        if count > lim:
            s = True

        # First attempt is very slow since we are trying to factor every possible number
        # if candidate%_lim == 0:
        #     count+=1
        #     for j in range(1, candidate):
        #         if candidate%j == 0:
        #             count+=1
        #         if count == _lim:
        #             s = True
        #             break
    return count

if __name__ == '__main__':
    print("{}".format(run(4)))