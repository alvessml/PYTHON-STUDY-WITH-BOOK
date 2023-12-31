s1 = input("Digite qualquer letra: ")
s2 = input("Digite novamente qualquer letra: ")

s3 = ""

for letra in s1:
    if letra not in s2 and letra not in s3:
        s3 += letra
for letra in s2:
    if letra not in s1 and letra not in s3:
        s3 += letra


if s3 == "":
    print("Caracteres incomuns não ecncontrado!")
else:
    print(f"Caracteres incomuns são: {s3}")
