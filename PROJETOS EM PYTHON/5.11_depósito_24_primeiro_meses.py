d_inicial = float(input("Digite seu depósito inicial: R$"))
d_mensal = float(input("Digite seu depósito mensal: R$"))
taxa = float(input("Qual o percentual de juros da poupança ao mês? "))
mês = 1
saldo = d_inicial
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R${saldo:.2f}")
    mês = mês + 1
print(f"Ao mês 24 o juros total obtido será de R${saldo - d_inicial:.2f}")
