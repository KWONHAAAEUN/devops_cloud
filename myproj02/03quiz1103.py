sum = 0
for number in range(1, 100):
    if (number % 3 == 0) and (number % 5 == 0):
        sum += number
print(sum)
