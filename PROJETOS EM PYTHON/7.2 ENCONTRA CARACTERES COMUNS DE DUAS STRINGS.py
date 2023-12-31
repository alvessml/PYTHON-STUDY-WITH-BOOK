s1 = input("Digite uma string qualquer: ")
s2 = input("Digite outra string para comparar com a de cima: ")

s3 = ""
for letra in s1:
    # SE CADA LETRA DA STRING 1 ESTIVER NA SEGUNDA STRING E NÃO ESTIVER
    # NA TERCEIRA STRING, SERÁ ADICIONADO NA TERCEIRA STRING!
    if letra in s2 and letra not in s3:
        s3 += letra

if s3 == "":
    print("Nenhum caracteres em comum encontrado!")
else:
    print(f"Caracteres em comuns são: {s3}.")
