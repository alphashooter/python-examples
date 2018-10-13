def fibonacci(n_):
    result = [0, 1]
    while len(result) < n_:
        result.append(result[-2] + result[-1])
    return result


n = input('Введите n: ')
n = int(n)

values = fibonacci(n)
for i in range(n):  # range(n) = 0, 1, 2, ..., n - 1
    print('x%d = %d' % (i + 1, values[i]))
