def múltiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))

print(f"{x1} é múltiplo de {x2}?", múltiplo(x1, x2))
