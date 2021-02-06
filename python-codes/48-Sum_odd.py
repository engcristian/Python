# Summing all odd numbers that are multiples of 3 and counting it
sum = 0
count = 0
for c in range(3, 501, 6):
    sum += c
    count += 1
    print(c)
print(sum, count)