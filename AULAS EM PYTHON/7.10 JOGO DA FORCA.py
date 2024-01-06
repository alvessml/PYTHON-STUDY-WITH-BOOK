palavra = input("Digite a palavra secreta: ").lower().strip()

for x in range(50):
    print()
print("--"*30)
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        # SE ACERTAR A SENHA VAI IGUAL A MINHA LETRA, SE NÃO IRÁ PERMANECER OS " . ". #
        senha += letra if letra in acertos else "."
    print(f"senha: {senha}")

    # SE MINHA SENHA ESTIVER IGUAL A PALAVRA, ENTÃO EU ACERTEI TODAS, DEPOIS IRÁ FINALIZAR! #
    if senha == palavra:
        print("--"*30)
        print("Você acertou!")
        break

    # COMEÇO DA FOCA, APÓS DIGITAR A PALAVRA PARA ADIVINHAR. #
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    # CÓDIGO PARA SABER SE A MINHA TENTATIVA ESTÁ EM PALVRA, SE SIM
    # ELE VAI JOGAR PARA MINHA LISTA ACERTOS! Se não irá jogar para
    # a lsita de erros.
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você erro!")

    # DESENHO DO BONECO DA FORCA.
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "

    elif erros == 3:
        linha2 = " /|  "
    elif erros >= 4:
        linha2 = " /|\ "
    # IRÁ PRINTAR AS PARTES DO CORPO ACIMA DAS PERNAS. #
    print("X%s" % linha2)

    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "
    # IRÁ PRINTAR AS PARTES AS PERNAS. #
    print("X%s" % linha3)

    # IRÁ PRINTAR O CHÃO. #
    print("X\n===========")
    if erros == 6:
        print("\nEnforcado!!!")
        break
