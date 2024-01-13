# IRÁ´MOSTRAR QUAL ÍNDICE O MEU VALOR ESTÁ NA LISTA.

def pesquisa(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


L = [10, 20, 25, 30]
print(pesquisa(L, 25))
print(pesquisa(L, 27))
