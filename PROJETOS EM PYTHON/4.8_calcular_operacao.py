d1 = float(input("Digite o primeiro número: "))
d2 = float(input("Digite o segundo número: "))
print("-=" * 30 )
print("""[1] Adição 
[2] Subtração
[3] Multiplicação
[4] Divisão""")
ope = int(input("Qual operação você quer executar? "))
if ope == 1:
    print(f"A adição será {d1} + {d2} = {d1 + d2:.2f}")
elif ope == 2:
    print(f"A subtração será {d1} - {d2} = {d1 - d2:.2f}")
elif ope == 3:
    print(f"A multiplicação será {d1} x {d2} = {d1 * d2}")
elif ope == 4:
    print(f"A divisão será {d1} / {d2} = {d1 / d2:.2f}")
else:
    print("Informção inválida! Digite um número de 1 a 4.")
