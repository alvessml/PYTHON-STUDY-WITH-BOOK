import sys

if len(sys.argv) != 2:
    print("\nUso: e09-01.py nom_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        print(linha[:-1])
    arquivo.close()
