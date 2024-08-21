salário = float(input("Diga o salário do funcionário: "))
if salário > 1250:
    print("o seu salário atual agora é R${}".format(salário * 0.1 + salário))
else:
    print("o seu salário atual agora é R${}".format(salário * 0.15 + salário))    