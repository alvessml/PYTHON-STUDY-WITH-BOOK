arquivo = input("Digite o nome do arquivo para abrir: ")

for linha in open(arquivo.readlines()):
    print(linha)

arquivo.close