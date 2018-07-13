def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

if __name__ == "__main__":
    print("Enter 2 numbers to calculate GCD: ")
    a,b = map(int, input().split())
    print("GCD is {}".format(gcd(a,b)))
