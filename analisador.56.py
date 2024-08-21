from datetime import date
data = date.today().year
velho = 0
nomevelho = ''
contador = 0
soma = 0
for i in range(0,4):
    print("====={}°Pessoa=====".format(i+1))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("M/F: ")).strip().upper()[0]
    if i == 1 and sexo in "M":
        velho = idade
        nomevelho = nome
    if sexo in 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    soma += idade
    media = soma / 4
    if idade < 20 and sexo in "F":
        contador += 1
print("A média da idade do grupo é {}".format(media))
print("O Homem mais velho tem {} anos e seu nome é {}".format(velho, nomevelho))
print("O número de mulheres com idade menor que 20 é {}".format(contador))
