erros = 6

print("X==:==\nX  :  ")
print("X  O  " if erros >= 1 else "X")
linha2 = ""
if erros == 2:
    linha2 = " | "
elif erros == 3:
    linha2 = " /| "
elif erros >= 4:
    linha2 = " /|\ "
print("X%s" % linha2)

linha3 = ""
if erros == 5:
    linha3 += " /   "
elif erros >= 6:
    linha3 += " / \ "
print("X%s" % linha3)
print("X\n==========")
