dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente += 1
resto = x
print(f"A divisão de {dividendo:.2f} / {divisor:.2f} = {quociente:.2f} e terá resto = {resto:.2f}")
    