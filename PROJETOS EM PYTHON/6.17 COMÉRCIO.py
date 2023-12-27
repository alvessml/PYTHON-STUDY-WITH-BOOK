def comercio():
    estoque = {"tomate": [1000, 2.30],
               "alface": [500, 0.45],
               "batata": [200, 1.20],
               "feijão": [100, 8.60]}
    print(f"""
    ----COMÉRCIO-----
    [1] Tomate: R$2,30 - estoque {estoque["tomate"][0]}
    [2] Alface: R$0,45 - estoque {estoque["alface"][0]}
    [3] Batata: R$1,20 - estoque {estoque["batata"][0]}
    [4] Feijão: R$8,60 - estoque {estoque["feijão"][0]}
    [5] Sair
            """)

    compra = []
    while True:
        produto = int(
            input("Digite o némero do produto desejado [1][2][3][4] ou [5] para sair: "))
        if produto >= 5:
            break
        quantidade = int(input("Quantidade: "))

        if produto == 1:
            compra.append(["tomate", quantidade])
        elif produto == 2:
            compra.append(["alface", quantidade])
        elif produto == 3:
            compra.append(["batata", quantidade])
        elif produto == 4:
            compra.append(["feijão", quantidade])

    return estoque, compra


def processo(estoque, compra):

    print("-=" * 30)
    print("\nVendas realizada: \n")

    total = 0
    for venda in compra:
        produto, quantidade = venda
        preco = estoque[produto][1]
        custo = preco * quantidade
        print(f"{produto}: {quantidade} x R${preco:.2f} = R${custo:.2f}")
        estoque[produto][0] -= quantidade
        total += custo
    print("\n")
    return estoque


def main():
    estoque, compra = comercio()
    estoque = processo(estoque, compra)

    print("-=" * 30)
    print("Estoque disponível no momento:\n")

    for chave, dados in estoque.items():
        print(f"Descrição: {chave}")
        print(f"Quantidade: {dados[0]}")
        print("Preço: {:.2f} \n".format(dados[1]))


main()
