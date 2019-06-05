from math import sin

x = float(input('x = '))
n = int(input('n = '))

result = x
term = x
for i in range(1, n):
    term *= -(x * x) / (2 * i * (2 * i + 1))
    result += term

print(f'{result} ({sin(x)})')
