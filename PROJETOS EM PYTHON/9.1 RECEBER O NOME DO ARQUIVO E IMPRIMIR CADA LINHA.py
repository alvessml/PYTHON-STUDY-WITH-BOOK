nome = input("Digite o nome do arquivo para abrir: ")

arquivo = open(nome, "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close