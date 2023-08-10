print("-=" * 15, "APROVAÇÃO DE EMPRÉSTIMO PARA ADIQUIRIR UMA CASA", "-=" * 15)
casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos? "))
prestacao_max = salario * 0.3
prestacao = casa / (anos * 12)
if prestacao <= prestacao_max:
    print(
        f"Emprestimo APROVADO!!! Sua prestação mensal será de R${prestacao:.2f}")
else:
    print(f"Emprestimo NEGADO! Sua prestação mensal seria de R${prestacao:.2f}")
