def maior(a, b):
    if a >= b:
        return a
    else:
        return b

x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))

print("O maior número é", maior(x1, x2))
