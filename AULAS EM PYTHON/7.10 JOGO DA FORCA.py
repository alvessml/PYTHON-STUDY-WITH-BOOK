palavra = input("Digite a palavra secreta: ").lower().strip()

for x in range(100):
    print()

digitadas = []
acertos = []
erros = []
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\n Digite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você erro!")

    # DESENHO DO BONECO DA FORCA!
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
