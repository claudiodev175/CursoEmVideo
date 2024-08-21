from datetime import date
ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print("Você deve se alistar, imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print("você não tem 18 anos ainda faltam {}".format(saldo))
elif idade > 18:
    saldo = idade - 18
    print("você deveria ter se alistado a {} anos".format(saldo))