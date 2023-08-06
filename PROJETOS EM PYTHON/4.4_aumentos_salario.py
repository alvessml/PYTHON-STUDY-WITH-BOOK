salario = float(input("Qual é o seu salário? "))
if salario > 1250:
    novo = salario + (salario * 0.1)
    print(f"Seu novo salario será R${novo:.2f}!")
else:
    novo = salario + (salario * 0.15)
    print(f"Seu novo salário será R${novo:.2f}!")
