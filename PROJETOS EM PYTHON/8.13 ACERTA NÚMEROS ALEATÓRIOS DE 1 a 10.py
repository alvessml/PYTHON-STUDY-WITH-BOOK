from random import randint 
L = [randint(1, 10) for _ in range(10)]
while True:
    n = int(input("Digite um número para advinhar os que estão na lista gerada: "))
    if n