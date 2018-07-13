list = [1,2]

while True:
    new_number = list[-1] + list[-2]
    list.append(new_number)
    if list[-1] > 4000000:
        list.pop(-1)
        break

sum = 0
for i in list:
    if i%2 != 0: continue
    sum += i

print(sum)
