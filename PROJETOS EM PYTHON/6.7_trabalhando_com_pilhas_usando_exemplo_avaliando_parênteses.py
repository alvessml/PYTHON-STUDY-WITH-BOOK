expressão = input("Digite a sequência de parênteses a validar: ")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if espressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força uma mensagem de erro!
            break
    x += 1
if len(pilha) == 0:
    print("OK!!!")
else:
    print("ERRO!")
