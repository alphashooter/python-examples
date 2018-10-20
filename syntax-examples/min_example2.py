def min(seq):
    result = seq[0]
    for i in range(1, len(seq)):
        if seq[i] < result:
            result = seq[i]
    return result


string = '312'
print(min(string))
