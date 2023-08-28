notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input("Nota: "))
    soma += notas[x]
    x += 1
x = 0
print("=-" * 15, "Média artitmética", "-=" * 15)
while x < 7:
    print(f"Nota {x + 1}: {notas[x]:.2f}")
    x += 1
print(f"Médias das notas: {soma / x:.2f}")
