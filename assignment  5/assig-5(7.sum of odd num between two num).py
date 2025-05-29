start, end = 1, 10
sum = 0
i = start
while i <= end:
    if i % 2 != 0:
        sum += i
    i += 1
print("Sum of odd numbers:", sum)
