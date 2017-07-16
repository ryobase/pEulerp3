""" Problem 2: 
Find the sum of all even Fibonacci sequence of whose value does not exceed four million """

import common

# Since the Fibonacci sequence is basically a list comprise of sum of the current value and 
# the next. we can just bruteforce to get the finally answer
def run():
    res = 0
    prev = 1
    cur = 2
    while prev <= 4000000:
        if not common.isOdd(prev):
            res+=prev
        temp = prev
        prev = cur
        cur = temp + cur
    return res

if __name__ == '__main__':
    print("{}".format(run()))