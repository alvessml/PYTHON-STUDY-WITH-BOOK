ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
while True:
    print(f"""Existem {len(fila1)} na fila A e {fila2} na fila B; 
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
        if operação == "A":
            if len(fila1) > 0:
                
