from typing import List


def read_file(path: str) -> List[int]:
    file = open(path, 'r')
    print(f'file {path} opened')

    result = []
    try:
        # Если в этом блоке возникнет исключение,
        # то оно не будет обработано, поскольку
        # здесь отсутствует блок except.
        # Но независимо от того, произошла ошибка
        # или нет, блок finally всегда выполнится
        for line in file:
            result.append(int(line))
    finally:
        file.close()
        print(f'file {path} closed')

    return result


try:
    numbers = read_file('try_example2_ok.txt')
    # numbers = read_file('try_example2_error.txt')
except ValueError as exc:
    print(f'Error: {exc}')
else:
    print(numbers)
