ESPAÇOS_POR_NÍVEL = 3

def imprime_elementos(l, nivel = 0):
    espaços = " " * ESPAÇOS_POR_NÍVEL * nivel
    
    if type(l) == list:
        print(espaços, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espaços, "]")
    else:
        print(espaços, l)

L = [1, [2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)