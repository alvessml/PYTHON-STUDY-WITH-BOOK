último = 10
fila = list(range(1, último + 1))
while True:
    print(f"Existem {len(fila)} clientes na fila.")
    print("Fila atual: ".format(fila))
    print("""Digite: 
          [F] para adicionar um cliente na fila;
          [A] para realizar o atendimento;
          [S] para sair.""")
    operação = input("Operação (F, A ou S): ") #AAFS
    x = 0
    sair = False
    while x < len(operação): 
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
                print("-=" * 30)
            else:
                print("Fila vazia! Ninguém para atender.")
                print("-=" * 30)
        elif operação[x] == "F":
            último += 1
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
            print("-=" * 30)
        x += 1
    if sair:
        break
