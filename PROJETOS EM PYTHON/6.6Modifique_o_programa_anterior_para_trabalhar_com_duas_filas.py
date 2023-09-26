ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
while True:
    print(f"""Existem {len(fila1)} na fila A e {len(fila2)} na fila B; 
          Fila A atual: {fila1};
          Fila B atual: {fila2}.
          
          Digite:
          [F] para adicionar um cliente na fila 1;
          [G] para adicionar um cliente na fila 2;
          [A] para realizar um atendimento na fila 1;
          [B] para realizar um atendimento na fila 2;
          [S] para sair.""")
    operação = input("Digite F, G, A, B ou S: ")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} da fila 1 atendido. ")
                print("-=" * 30)
            else:
                print("Fila vazia! Ninguém para atender.")
                print("-=" * 30)
        elif operação[x] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} da fila 2 atendido.")
                print("-=" * 30)
            else:
                print("Fila vazia! Ninguém para atender.")
                print("-=" * 30)
        elif operação[x] == "F":
            ultimo1 += 1
            fila1.append(ultimo1)
        elif operação[x] == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite somente A, B, F, G ou S")
            print("-=" * 30)
        x += 1
    if sair:
        break
        
