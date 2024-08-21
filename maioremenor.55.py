maior = 0
menor = 0
for i in range(0,5):
    peso = float(input("Digite o peso da pessoa de n°{}: ".format(i + 1)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("o maior peso lido foi {}KG".format(maior))
print("o menor peso lido foi {}KG".format(menor))
