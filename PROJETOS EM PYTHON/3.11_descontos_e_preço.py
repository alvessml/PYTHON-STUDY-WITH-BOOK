mercadoria = float(input("Valor da mercadoria: R$"))
percentual = float(input("Percentual do desconto: "))
valor_total_com_desconto = mercadoria - (mercadoria * percentual)/100
desconto = (mercadoria * percentual)/100
print(f"O valor do desconto foi R${desconto:5.2f} e o valor a ser pago será R${valor_total_com_desconto}")
