s = input("Digite letras quaisquer: ")

di = {}
for letra in s:
    di[letra] = di.get(letra, 0) + 1

for chave, valor in di.items():
    print(f"{chave}: {valor}x")
