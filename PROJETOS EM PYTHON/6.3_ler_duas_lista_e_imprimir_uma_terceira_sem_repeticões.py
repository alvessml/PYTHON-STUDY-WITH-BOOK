l1 = []
l2 = []
while True:
    e = int(input("Digite um número para a primeira lista (0 para sair): "))
    if e == 0:
        break
    l1.append(e)
while True:
    e = int(input("Digite um número para a segunda lista (0 para sair): "))
    if e == 0:
        break
    l2.append(e)
l3 = []
l1l2 = l1[:]
l1l2.extend(l2)
x = 0
while x < len(l1l2):
    y = 0
    while y < len(l3):
        if l1l2[x] == l3[y]:
            break
        y += 1
    if y == len(l3):
        l3.append(l1l2[x])
    x += 1
x = 0
while x < len(l3):
    print(f"{x}: {l3[x]}")
    x += 1
