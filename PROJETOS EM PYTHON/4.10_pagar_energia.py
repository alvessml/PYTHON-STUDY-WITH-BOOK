print("-=" * 30)
consumo = float(input("Digite o seu consumo de energia em kWh: "))
print("""[R] Residencial
[C] Comercial
[I] Industrial""")
tipo = input("Qual sua instalação (R, C ou I)? ")
if tipo == "R" or "r":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C" or "c":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I" or "i":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro! Tipo de instalação desconhecida!")
valor = preco * consumo
print(f"Valor a pagar será de R${valor:.2f}")
