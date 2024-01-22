from random import randint 
L = []
x = 0
while x > 10:
    n = randint(1, 20)
    if n not in L:
        L.append(n)
        x += 1

print(L)