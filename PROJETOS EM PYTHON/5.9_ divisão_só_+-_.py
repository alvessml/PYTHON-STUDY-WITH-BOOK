dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = 0
x = dividendo
while x >=  divisor:
    x = x - divisor 
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente}")
print(f"E o resto será {resto}")
