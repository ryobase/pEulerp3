""" Problem 5: 
Find the least common multiple of 1 to 20 """

import common

# Since gcd always return a value of which is can be used to evenly divide
# both iterator and accumulator we can use it to get the products of least common multiple
# of natural numbers 1 to 20
# https://en.wikipedia.org/wiki/Least_common_multiple
def run(n):
    res = 1
    for i in range(1, n):
        res *= (i//common.gcd(res, i))
    return res

if __name__ == '__main__':
    print("{}".format(run(20)))