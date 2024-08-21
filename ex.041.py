from datetime import date
ano = int(input("Ano de nascimento: "))
atual = date.today().year
print("o atleta tem {} anos".format(atual - ano))
if atual - ano <= 9:
    print("Classificação: Mirim")
elif atual - ano > 9 and atual - ano <= 14:
    print("Classificação: Infantil")
elif atual - ano > 14 and atual - ano <= 19:
    print("Classificação: Júnior")
elif atual - ano > 19 and atual - ano <= 25:
    print("Classificação: Sênior")
elif atual - ano > 25:
    print("Classificação: Master")