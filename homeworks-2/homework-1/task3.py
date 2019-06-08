n = int(input('n = '))

seq = []
for i in range(n):
    x = int(input(f'x{i + 1} = '))
    if x == 0:
        seq.insert(0, x)
    else:
        seq.append(x)

print(seq)
