velha = """                 posições
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


for _ in tabuleiro:
    print(_)