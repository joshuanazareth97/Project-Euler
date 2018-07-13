from isPrime import isPrime
n = int(input("Enter number to find largest prime factor: "))
i = 2
largest = 0
while(i*i<n):
    if not (n%i):
        if(isPrime(i)):
            largest = i
        if(isPrime(n/i)):
            largest = n/i
            break
    i += 1

print(largest)
