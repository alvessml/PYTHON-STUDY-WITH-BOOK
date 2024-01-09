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

indice = int(input("Digite um número: "))
palavra = palavras[(indice * 776) % len(palavras)]

for _ in range(100):
    print()

digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :    
X        
X       
X       
X       
========

"""
linhas = []
#                      "QUEBRA A STRING EM VÁRIAS LINHAS"
for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(f"{senha}")

    if senha == palavra:
        print("\nAcertou!!!")
        break

    tentativa = input("Digite uma letra: ")

    if tentativa in digitadas:
        print("Já digitou esta letra! Tente novamente outra.")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa

        else:
            erros += 1
            print("Você errou!")
            print("-="*15)
            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "/"
            elif erros == 4:
                linhas[4][4] = "\\"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"

    for l in linhas:
        # O método Join irá printar cada conjunto da minha
        # linha da lista, completo!
        print("".join(l))

    if erros == 6:
        print("Eforcado!!!")
        print(f"A palavra secreta era: {palavra}")
        break
