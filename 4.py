'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time



start = time.time()
largest = 0
for i in range(100,999):
    for j in range(100,i):
        product = i*j
        if product > largest and str(product) == str(product)[::-1]:
            largest = product

print(largest)

end = time.time()
print("Executed in {0:5f} ms".format((end - start)*1000))
