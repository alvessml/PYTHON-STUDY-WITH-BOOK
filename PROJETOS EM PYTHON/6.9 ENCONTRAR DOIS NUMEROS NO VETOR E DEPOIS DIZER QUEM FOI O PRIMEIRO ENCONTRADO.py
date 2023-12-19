from random import randint 
L = [randint(1, 20) for _ in range(10)]

sem_repetição = set(L)

lista_sem_repetição = list(sem_repetição)

print(lista_sem_repetição)

num_1 = int(input("Digite um número: "))

num_2 = int(input("Digite um número: "))

x1 = 0
while x1 < len(lista_sem_repetição):
    if num_1 == lista_sem_repetição[x1]:
        break
    x1 += 1

x2 = 0
while x2 < len(lista_sem_repetição):
    if num_2 == lista_sem_repetição[x2]:
        break
    x2 += 1

if x1 < len(lista_sem_repetição) and x2 == len(lista_sem_repetição):
    print(f"{num_1} achado na posição {x1}")
    print(f"{num_2} não achado!")
elif x2 < len(lista_sem_repetição) and x1 == len(lista_sem_repetição):
    print(f"{num_1} não achado!")
    print(f"{num_2} achado na posição {x2}")
else:
    if x1 < x2:
        print(f"\nPrimeiro achado foi o {num_1} na posição {x1}")
        print(f"\nDepois o {num_2} na posição {x2}")
    elif x2 < x1:
        print(f"\nPrimeiro achado foi o {num_2} na posição {x2}")
        print(f"\nDepois o {num_1} na posição {x1}")