n = int(input('Введите n: '))

numbers = [i for i in range(1, n)]

i = 1
while numbers[i] < n / 2:
    for j in range(len(numbers) - 1, i, -1):
        if numbers[j] % numbers[i] == 0:
            del numbers[j]
    i += 1

print(numbers)
