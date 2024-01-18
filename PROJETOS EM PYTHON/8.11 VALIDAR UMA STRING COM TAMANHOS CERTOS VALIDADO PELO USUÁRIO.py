def validacao(s, mínimo, máximo):
    tamanho = len(s)    
    return mínimo <= tamanho <= máximo

print(validacao("SAMUEL", 2, 9))
print(validacao("Levi", 5, 6))