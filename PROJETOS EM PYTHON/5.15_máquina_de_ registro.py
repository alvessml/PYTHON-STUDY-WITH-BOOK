# c = código
# x = preço
# q = quantidade
print("-="*30)
pagar = 0
while True:
    c = int(input("Digite o código do produto de: "))
    preço = 0
    if c == 1:
        preço += 0.5
    elif c == 2:
        preço += 1
    elif c == 3:
        preço += 4
    elif c == 5:
        preço += 7
    elif c == 9:
        preço += 8
    elif c == 0:
        break
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        pagar = pagar + (preço * quantidade)
print("-="*30)
print(f"O total de compras será R${pagar:.2f}")
