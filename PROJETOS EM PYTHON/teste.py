from random import randint 

print("=-"*10+"JOGO DA VELHA".center(20)+"-="*10)

matriz = [[x]*3 for x in range(3)]
escolhido = []
while True: 

    posição1 = int(input("Digite qual local você vai jogar: "))
    if posição1 in escolhido:
        print("Já foi jogado neste loca! insire outro local !")
        continue
    jogador1 = input("Digite (X ou O): ")

    posição2 = int(input("Digite qual local você vai jogar: "))
    if posição2 in escolhido:
        print("Já foi jogado neste loca! insire outro local !")
        continue
    jogador2 = input("Digite (X ou O): ")
