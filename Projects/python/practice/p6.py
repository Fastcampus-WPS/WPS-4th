def make_gugu():    ret = []
    for i in range(2, 10):
        for j in range(1, 10):
            ret.append('{} x {} = {}'.format(i, j, i * j))
    return ret

def make_gugu2():
    return [(lambda a, b : '{} x {} = {}'.format(a, b, a*b))(x, y) for x in range(2, 10) for y in range(1, 10)]

def make_gugu3():
    return ['{} x {} = {}'.format(x, y, x * y) for x in range(2, 10) for y in range(1, 10)]

result = make_gugu3()
print(result)
result_str = '\n'.join(result)
print(result_str)
