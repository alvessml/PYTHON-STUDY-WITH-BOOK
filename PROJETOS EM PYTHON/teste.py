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

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

print(linhas)
