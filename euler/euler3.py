""" Problem 5:
Find the prime factor of number 600851475143 """

import common

# Here we are bruteforcing our way to acheive the goal. Since prime number can only be 
# divided by 1 and itself, we can just keep loop until the final result is a prime
def run(n):
    t = 2
    arr = []
    while not common.isPrime(n):
        if t == 2 and n%t != 0:
            t+=1
        elif n%t != 0:
            t+=2
            if not common.isPrime(t):
                t+=2
        if n%t == 0:
            n //= t
            arr.append(t)
    arr.append(n)
    return max(arr)

if __name__ == '__main__':
    print("{}".format(run(600851475143)))