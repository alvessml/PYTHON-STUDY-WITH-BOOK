km_carro = float(input("Qual a velocidade do carro? "))
if km_carro > 80:
    multa = (km_carro - 80) * 5
    print(f"Você ultrapassou a velocidade de 80km, você sofrerá uma multa de R${multa:5.2f} por ultrapassar!")
else:
    print("Você não ultrapassou a velocidade de 80km")
    