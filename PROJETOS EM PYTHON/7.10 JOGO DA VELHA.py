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

# Posições que leva o jogador a ganhar o jogo!
ganho = [
    [1, 2, 3],  # Linhas
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],  # Colunas
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],  # Diagonais
    [1, 5, 9]
]

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))


jogador = "X"  # Começa jogando com X
jogando = True
jogadas = 0

while True:
    for t in tabuleiro:  # Imprime o tabuleiro
        # (map(str, t)) Converte cada elemento "t" da lista para uma string.
        
        print("".join(map(str, t)))

    if not jogando:  # Termina após imprimir o tabuleiro final
        break

    if jogadas == 9:  # Dará velha
        print("Deu velha!!! Ninguém ganhou.")
        break

    jogada = int(
        input(f"Digite a posição a jogar 1 á 9 (jogador {jogador}): "))

    # Jogada sempre terá que está entre 1 a 9.
    if jogada < 1 or jogada > 9:
        print("Posição inválida")
        continue

    # Irá verificar se a posição está livre.
# Ex:jogad = 1 tabuleiro [    5     ] [         1     ] (*Primeira)
# posição, irá verificar se está vazia ou não.
    if tabuleiro[posições[jogada][0]][posições[jogada][1]] != " ":
        print("Posição ocupada.")
        continue

    # Marca a jogada do jogador na velha
    tabuleiro[posições[jogada][0]][posições[jogada][1]] = jogada

    # -------------------------------------------------------------#
    # Verificar se ganhou
    for p in ganho:
        for x in p:
            if tabuleiro[posições[x][0]][posições[x][1]] != jogador:
                break

        # Verificar se o for termina sem break, todas as posições
        # de p pertencem ao mesmo jogador!
        else:
            print(f"O jogador {jogador} ganhou ({p}): ")
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O"  # Alternar os jogadores
    jogadas += 1
