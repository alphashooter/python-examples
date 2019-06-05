n = int(input('Введите n: '))

numbers = [i for i in range(1, n)]
for i in range(1, n - 1):
    if numbers[i] == 0:
        continue
    for j in range(i + 1, n - 1):
        if numbers[j] % numbers[i] == 0:
            numbers[j] = 0

print(numbers)

numbers = list(filter(lambda x: x > 0, numbers))
print(numbers)
