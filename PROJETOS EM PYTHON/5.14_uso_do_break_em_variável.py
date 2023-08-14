s = 0
q = 0
while True:
    n = float(input("Digite um número e 0 para PARAR: "))
    if n == 0:
        break
    s += n
    q += 1
print(f"A quantidade de números digitados é {q}")
print(f"A soma desse números será {s}")
print(f"A média aritmética será {s / (q) :.2f}")
