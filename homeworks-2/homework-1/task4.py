from math import cos

x = float(input('x = '))
n = int(input('n = '))

result = 1
term = 1
for i in range(1, n):
    term *= -(x * x) / (2 * i * (2 * i - 1))
    result += term

print(f'{result} ({cos(x)})')
