salario = float(input("Digite seu salário para calcular o imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Seu salário é R${salario:.2f}, imposto a pagar é R${imposto:.2f}!")