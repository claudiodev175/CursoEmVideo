from datetime import date
data = date.today().year
contador1 = 0
contador2 = 0
for i in range(0,7):
    ano = int(input("Digite o ano que a pessoa de n.{} nasceu: ".format(i+1)))
    idade = data - ano
    if idade < 21:
        contador1 += 1
    else:
        contador2 += 1
print("Temos {} pessoas menores de idade".format(contador1))
print("Temos {} pessoas maiores de idade".format(contador2))
        