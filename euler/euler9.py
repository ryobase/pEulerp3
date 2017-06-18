""" Problem 9:
Find the product abc of which is a Pythagorean triplet and a+b+c=1000 """

# Here we use Euclid's Formula to practically bruteforce our way to get the final answer
# Pythagorean triplets can be generated using a pair of two values such that m > n > 0
# https://www.grc.nasa.gov/www/k-12/Numbers/Math/Mathematical_Thinking/pythtrip.htm
def run(limit):
    o = True
    m = 2
    while o is True:
        m+=1
        for i in range(1,m-1):
            a = 2*(m*i)
            b = (m*m)-(i*i)
            c = (m*m)+(i*i)
            if (a+b+c) == limit:
                o = False
                break
    return (a*b*c)

if __name__ == '__main__':
    print("{}".format(run(1000)))