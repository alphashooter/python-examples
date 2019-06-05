s = input('Введите выражение: ')

tokens = []
while True:
    for i in range(len(s)):
        if s[i] not in {'+', '-', '*', '/'}:
            continue
        tokens += float(s[:i]), s[i]
        s = s[i+1:]
        break
    else:
        tokens += float(s),
        break

i = 1
while i < len(tokens) - 1:
    token = tokens[i]
    if token == '*':
        tokens[i - 1] *= tokens[i + 1]
        del tokens[i:i+2]
    elif token == '/':
        ...  # ваш код для /
    else:
        i += 1

...  # ваш код для + и -

assert len(tokens) == 1
print(tokens[0])
