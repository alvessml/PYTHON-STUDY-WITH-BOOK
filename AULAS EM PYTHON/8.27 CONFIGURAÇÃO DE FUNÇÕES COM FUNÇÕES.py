def imprime_lista(L, fimpresão, fcondição):
    for e in L:
        if fcondição(e):
            fimpresão

def imprime_elemento(e):
    print(f"Valor: {e}")

def épar(x):
    return x % 2 == 0

def éimpar(x):
    return not épar(x)

L = [1, 7, 9, 2, 11, 0]

print(imprime_lista(L, imprime_elemento, épar))
print(imprime_lista(L, imprime_elemento, éimpar))