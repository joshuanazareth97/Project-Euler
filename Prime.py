import math

def isPrime(n):
    i = 2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        else:
            i += 1
    return True

if __name__ == "__main__":
    n = int(input("Enter number to check for primality: "))
    if(isPrime(n)):
        print("{} is a Prime Number.".format(n))
    else:
        print("{} is not a Prime Number.".format(n))
