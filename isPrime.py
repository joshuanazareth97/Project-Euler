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
    count = int(input("Enter the position of prime number you want to generate(1st, 1000th etc): "))
    j = 0
    n = 0
    while(j<=count):
        n += 1
        if(isPrime(n)):
            j += 1

    print(n)
