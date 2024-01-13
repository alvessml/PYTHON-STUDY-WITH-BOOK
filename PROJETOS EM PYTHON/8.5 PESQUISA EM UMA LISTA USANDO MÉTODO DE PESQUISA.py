def pesquisa(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None


L = [343, 28, 73, 94]

print(pesquisa(L, 73))
