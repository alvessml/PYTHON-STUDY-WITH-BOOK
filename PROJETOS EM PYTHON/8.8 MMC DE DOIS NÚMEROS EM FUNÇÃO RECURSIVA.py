def mmc(a, b):
    if b == 0:
        return a
    return mmc(abs(a*b)/dc)