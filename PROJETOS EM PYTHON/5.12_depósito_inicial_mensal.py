d_inicial = float(input("Digite seu depósito inicial: R$"))
d_mensal = float(input("Digite seu depósito mensal: R$"))
taxa = float(input("Qual o percentual da taxa mensal? "))
mês = 1
saldo = d_inicial
while mês <= 24:
    saldo = saldo * (saldo * (taxa / 100))
    print(f"O saldo do mês {mês} é de R${saldo:.2f}")
    mês = mês + 1
