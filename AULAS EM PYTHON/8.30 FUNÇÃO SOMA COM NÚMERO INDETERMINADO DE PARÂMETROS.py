def soma(*args):
    s = 0

    for x in args:
        s += x

    return s

print(soma(4, 4, 2, 5, 10))
