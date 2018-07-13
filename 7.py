'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import time
from Prime import isPrime

count = int(input("Enter the position of prime number you want to generate(1st, 1000th etc): "))

start = time.time()

j = 0
n = 0
while(j<=count):
    n += 1
    if(isPrime(n)):
        j += 1

print("The {0}th Prime Number is {1}".format(count,n))

end = time.time()
print("Executed in {0:5f} ms".format((end - start)*1000))
