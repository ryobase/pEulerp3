""" Problem 4: 
Find the largest Palindrome number of which is the product of two 3-digit numbers """

import common

# Since there is no efficient way to find Palindrome numbers
# here we are bruteforcing our way to solve the problem
def run():
    res = 0
    for i in range(100,1000):
        for j in range(100,1000):
            t = i*j
            if common.isPalindrome(t) and t > res:
                res = t
    return res

if __name__ == "__main__":
    print("{}".format(run()))