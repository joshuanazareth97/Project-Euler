from Prime import sieve

import time

print ("Sum of all Primes below 2 million:")

start = time.time()

primes = sieve(2000000)

sum = 0

for a,b in primes.items():
    if b:
        sum += a


print(sum)

end = time.time()
print("Executed in {0:5f} ms".format((end - start)*1000))
