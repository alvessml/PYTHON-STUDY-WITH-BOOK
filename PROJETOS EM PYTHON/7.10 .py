velha = """         POSIÇÕES
   |   |       7 | 8 | 9
---+---+---   ---+---+---
   |   |       4 | 5 | 6
---+---+---   ---+---+---
   |   |       1 | 2 | 3           

"""

posições = [
    None,    # Elemento adicionado para facilitar índices
    (5, 1),  # 1
    (5, 5),  # 2
    (5, 9),  # 3
    (3, 1),  # 4
    (3, 5),  # 5
    (3, 9),  # 6
    (1, 1),  # 7
    (1, 5),  # 8
    (1, 9)   # 9
    ]

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))


jagador = "X" # Começa jogando com X
jogando = True
jogadas = 0
while True:
    for t in tabuleiro:
        print("".join(t))
    
    if not jogando: # Termina após imprimir o tabuleiro final
        break

    if jogadas == 9: # Dará velha
        print("Deu velha!!! Ninguém ganhou.")
        break


    jogada = int(input(f"Digite a posiçãõ a jogar 1 á 9 (jogador {jogador}): "))
    
    if jogada < 1  or jogada > 9:
        print("Posição inválida")
        continue

    if tabuleiro[posições[]]