último = 10
fila = list(range(1, último, + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("""Digite:
          [F] Para adicionar um cliente ao fima da fila;
          [A] Para realizar um atendimento;
          [S] Para sair.""")
    operação = input("Digite (F, S ou A): ")
    if operação == A:
        if len(fila) > 0:
            atendido = fila.pop(0)
        print....

