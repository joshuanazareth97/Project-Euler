import time
from Prime import isPrime

n = int(input("Enter upper limit to find sum of primes: "))

start = time.time()

sum = 0
for i in range(2,n):
    if isPrime(i):
        sum += i
    i += 1

print("Sum of all primes below {0} = {1}".format(n,sum))

end = time.time()
print("Executed in {0:5f} ms".format((end - start)*1000))
