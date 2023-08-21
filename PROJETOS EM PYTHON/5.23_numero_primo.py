num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[32m", end="")
        tot += 1
    else:
        print("\033[31m", end="")
    print(f"{c}", end=" ")
print(f"\n\033[m O número {num} foi divisível {tot} vezes")
if tot == 2:
    print("Este número é PRIMO!")
else:
    print("Este número \033[31mNÃO\033[m é primo!")
