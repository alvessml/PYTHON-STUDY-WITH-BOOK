palavras = [
    "casa",
    "bola",
    "mangueira",
    "uva",
    "quiabo",
    "computador",
    "cobra",
    "lentilha",
    "arroz"
]

índice = int(input("Digite um numero: "))
palavra = palavras[(índice * 776) % len(palavras)]

for _ in range(100):
    print()

digitados = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()
    if tentativa in digitados:
        print("Você já digitou está letra!")
        continue
    else:
        digitados += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = " /   "
    elif erros == 3:
        linha2 = " / \ "
    elif erros >= 4:
        linha2 = " /|\ "
    print(f"X{linha2}")

    linha3 = ""
    if erros == 5:
        linha3 = " /   "
    elif erros >= 6:
        linha3 = " / \ "
    print(f"X{linha3}")

    print("X\n========")

    if erros == 6:
        print("Você foi enforcado!!")
        print(f"A palavra secreta era: {palavra}")
        break
