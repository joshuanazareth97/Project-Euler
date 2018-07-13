'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?

'''
from gcd import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

import time

start = time.time()

i = 12
a = 11
while(i<=20): #hardcording value as no time for optimization for higher vals of n
    a = lcm(a,i)
    i = i+1

print("LCM of 1,2,3,....,20 is {}".format(a))
end = time.time()
print("Executed in {0:5f} ms".format((end - start)*1000))
