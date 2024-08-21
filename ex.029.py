km = float(input("Qual a velocidade atual do seu carro? "))
if km <= 80:
    print("Continue Dirigindo com segurança")
else:
    print("Você ultrapassou o limite de 80Km/h")
    print("Você sofreu uma multa de R${}".format(7 * (km - 80)))    

   