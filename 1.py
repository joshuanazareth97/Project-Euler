n  = int(input("Enter number to count till: "))
sum = 0
for i in range(1,n):
    if i%3 == 0 or i%5 == 0:
        sum += i

print(sum)
