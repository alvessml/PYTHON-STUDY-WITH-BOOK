from ENTRADA import valida_inteiro #RENOMEI O MÓDULO .PY "8.34 ENTRADA" PARA SOMENTE "ENTRADA" FUNCIONAR !!!!

L = []
for x in range(10):
    L.append(valida_inteiro("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
