import random

x = random.sample(range(1, 11), 3)

print(x)

erro = 0
while True:
    n = int(input("Digite um número para advinhar os que estão na lista gerada: "))
    
    if erro == 2:
        break
    
    if n == list(x):
        print("Você acertou!")
        break
    else:
        print("Você errou")
        erro += 1
    