def comercio():
    estoque = {"tomate": [1000, 2.30],
               "alface": [500, 0.45],
               "batata": [200, 1.20],
               "feijão": [100, 8.60]}
    print("""
    ----COMÉRCIO-----
    [1] Tomate: R$2,30
    [2] Alface: R$0,45
    [3] Batata: R$1,20
    [4] Feijão: R$8,60
    [5] Sair
          """)

    compra = []
    while True:
        produto = int(
            input("Digite o némero do produto desejado [1][2][3][4] ou [5] para sair: "))
        if produto == 5:
            break
        quantidade = int(input("Quantidade: "))
        compra.append([produto, quantidade])

    return estoque, compra


def processo(estoque, compra):
    total = 0
    print("-=" * 30)
    print("\nVendas realizada: \n")
    for venda in compra:
        produto, quantidade = venda
        preco = estoque[1]
        custo = preco * quantidade
        print(f"{produto}: {quantidade} x R${preco:.2f} = R${custo:.2f}")
        estoque[produto - 1][0] -= quantidade
        total += custo
    return estoque


def main():
    estoque, compra = comercio()
    estoque = processo(estoque, compra)

    for chave, dados in estoque.items():
        print(f"Descrição: {chave}")
        print(f"Quantidade: {dados[0]}")
        print("Preço: %.2f\n" % dados[1])


main()
