""" Problem 1: 
Calculate sum of numbers bewteen 1-1000 of which is either divisible by 3 or 5 """

# Easy problem that is solvable via bruteforce
def run():
    return sum(i for i in range(1000) if (i%3 ==0 or i%5 ==0))

if __name__ == "__main__":
    print("{}".format(run()))