x = 0

while True:  # infinite loop
    x += 1
    if x % 2 == 0:
        continue
    if x == 5:
        break
    print('x = %d' % x)
