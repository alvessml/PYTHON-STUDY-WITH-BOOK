s1 = input("Digite quaisquer letras: ")
s2 = input("Digite somente letras que estão acima para remover: ")

s3 = ""
for letra in s1:
    if letra not in s2:
        s3 += letra

print(f"1° string: {s1}")
print(f"2° string: {s2}")
if s3 == "":
    print("Todas as letras foram removida!")
else:
    print(f"3° string: {s3}")
