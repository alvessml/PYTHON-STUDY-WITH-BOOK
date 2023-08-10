pontos = 0
questão = 1
x = 0  # quantas questões acertarei apartir de 0!
while questão <= 3:
    resposta = input(f"Digite a resposta da questão {questão}: ")
    if questão == 1 and (resposta == "B" or resposta == "b"):
        pontos = pontos + 1
        x = x + 1
    if questão == 2 and resposta == "A" or resposta == "a":
        pontos = pontos + 1
        x = x + 1
    if questão == 3 and resposta == "D" or resposta == "d":
        pontos = pontos + 1
        x = x + 1
    questão = questão + 1
print(f"Você acertou {x} e ganhou {pontos} pontos")
