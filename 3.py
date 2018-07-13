'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Execution time = 0.232 secs
'''

from isPrime import isPrime
import time
n = int(input("Enter number to find largest prime factor: "))
start = time.time()
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
end = time.time()
print("Executed in {} secs".format(end - start))
