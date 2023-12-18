from random import randint
L = [randint(1, 20) for _ in range(10)]

sem_repetição = set(L)

lista_sem_repetição = list(sem_repetição)

print(lista_sem_repetição)

num = int(input("Digite um número: "))

x = 0 
while x < len(lista_sem_repetição):
    if num == lista_sem_repetição[x]:
        break
    x += 1

if x < len(list(sem_repetição)):
    print(f"{num} achado na posição {x}")
else:
    print(f"{num} não achado!")