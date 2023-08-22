frase = input("Digite uma frase ou número: "). strip().upper()
caractere = frase.split()
junto = "".join(caractere)
inverso = ""
for simbolo in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[simbolo]
if inverso == junto:
    print("Temos um palídromo!")
else:
    print("A frase digitada não é um palíndromo!")
