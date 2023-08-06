c_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos? "))
vida_perdida_dias = c_por_dia * 0.00694
vida_perdida = vida_perdida_dias * anos * 365
print(f"Você já perdeu {vida_perdida:0.0f} dias de vida fumando!")
