import sys

argv = input("Digite seu nome: ")
argv1 = input("Digite sua data de nascimento: ")

sys.argv = argv, argv1

for n, p in enumerate(sys.argv):
    print(f"{p}", end=" ")
