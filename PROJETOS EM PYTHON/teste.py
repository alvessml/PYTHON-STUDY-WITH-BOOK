último = 10
fila = list(range(1, último + 1))
atendido = fila.pop(0)
último += 1
fila.append(último)
print(fila)
atendido = fila.pop(0)
print(fila)