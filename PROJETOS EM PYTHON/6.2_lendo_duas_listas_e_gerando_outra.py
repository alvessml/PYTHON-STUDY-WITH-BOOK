l1 = []
l2 = []
while True:
    e = int(input("Digite um número para a lista 1 (0 para sair): "))
    if e == 0:
        break
    l1.append(e)
while True:
    e = int(input("Digite um número para a lista 2 (0 para sair): "))
    if e == 0:
        break
    l2.append(e)
l3 = l1[:]
l3.extend(l2)
x = 0
while x < len(l3):
    print(f"{x}: {l3[x]}")
    x += 1

