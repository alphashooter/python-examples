s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')


result = False
if len(s1) > len(s2):
    for i in range(1 + len(s1) - len(s2)):
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                break
        else:
            result = True
            break

if result:
    print('Строка "%s" является подстрокой "%s"' % (s2, s1))
else:
    print('Строка "%s" не является подстрокой "%s"' % (s2, s1))
