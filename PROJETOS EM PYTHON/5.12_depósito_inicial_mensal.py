d_inicial = float(input("Digite seu depósito inicial: R$"))
taxa = float(input("Qual o percentual da taxa mensal? "))
d_mensal = float(input("Digite seu depósito mensal: R$"))
mês = 1
saldo = d_inicial
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + d_mensal
    print(f"O saldo do mês {mês} é de R${saldo:.2f}")
    mês = mês + 1
print(f"Ao mês 24 o juros total obtido será de R${saldo - d_inicial:.2f}")
