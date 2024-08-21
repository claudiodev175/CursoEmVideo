contador1 = 0
contador2 = 0
contador3 = 0
while True:
    print("-="*20)
    print("CADASTRE UMA PESSOA")
    print("-="*20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        print("-="*20)
        sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
        print("-="*20)
    escolha = ' '
    while escolha not in "SN":
        escolha = str(input("Quer continuar[S/N]? ")).strip().upper()[0]
    if idade > 18:
        contador1 += 1
    if sexo in "M":
        contador2 += 1
    if sexo in "F" and idade > 20:
        contador3 += 1
    if escolha in "N":
        break
print(f"Possuimos {contador1} pessoa(s) maior(es) de idade")
print(f"Entre os cadastrados temos {contador2} homen(s)")
print(f"Foram um total de {contador3} mulhere(s) acima de 20 anos")
print("FIM DO PROGRAMA")
    
    