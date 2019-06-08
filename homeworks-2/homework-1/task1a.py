s = input('Введите строку: ')

result = True
for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
        result = False
        break

print(result)
