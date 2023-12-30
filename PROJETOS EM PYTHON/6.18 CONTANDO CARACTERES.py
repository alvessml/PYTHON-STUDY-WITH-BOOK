word = input(
    "Digite uma frase ou palavra, para saber quantas letras há repetida pelo dicionário: ")
d = {}
for letra in word:
    if letra == " ":
        False
    else:
        d[letra] = d.get(letra, 0) + 1
print(d)
