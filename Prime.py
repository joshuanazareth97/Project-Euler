import math

def isPrime(n):
    i = 2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        else:
            i += 1
    return True

def sieve(n):
    p_n = {}
    for i in range(2,n):
        p_n[i] = True
    for j in range(2,n):
        if p_n[j] == True:
            for a in range(2*j,n,j):
                p_n[a] = False
    return p_n


if __name__ == "__main__":
#    n = int(input("Enter number to check for primality: "))
#    if(isPrime(n)):
#        print("{} is a Prime Number.".format(n))
#    else:
#        print("{} is not a Prime Number.".format(n))
    test = sieve(2000000)
    n = int(input("Enter n < 2000000 to check for primality:"))
    print("{} is".format(n),end=" ")
    if not test[n]: print("not", end = " ")
    print("prime.")
