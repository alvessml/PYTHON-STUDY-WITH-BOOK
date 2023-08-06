km = int(input("Quantos km você andou no carro? "))
dias = int(input("Em quantos dias? "))
valor_a_pagar = km * 0.25 + dias*60
print(f"Valor a pagar pelo carro alugado será de R${valor_a_pagar:5.2f}")