s1 = input("Digite quaisquer letras: ")
s2 = input("Digite quais letras acima seleciono para ser substituído: ")
s3 = input("Quais letras para ser substituído: ")

if len(s2) == len(s3):
    res = ""
    for letra in s1:
        # Se minha letra do s1 foi encontrado em uma das posiçoes do s2
        # então letra receberá a posição encontrada do s2 seja 0, 1, 2,...
        posição = s2.find(letra)
        if posição != -1:
            # Se posição for encontrada em s2, res receberá a posição 0, 1,
            # 2,... do s2, e substituirá pela mesma posição mais só que o s3.
            # Exmplo:
            #   letra A == posição 0 do meu s2 que é A.
            #   terceira[posição = 0] do meu s3 escolhido para substituir
            #   exemplo o B.
            #   res receberá B no lugar de A
            res += s3[posição]
        else:
            res += letra
    print(f"1° string: {s1}")
    print(f"2° string: {s2}")
    print(f"3° string: {s3}")
    print(f"Resultado: {res}")

else:
    print("ERRO!!! A string 2 e 3 tem que ser do mesmo tamanho!")
