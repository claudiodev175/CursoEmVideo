valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos vai financiar a casa? "))
meses = anos * 12
prestação = valor / meses

if prestação > salario * 0.3:
    print("Para pagar uma casa de {:.2f} em {:.2f} anos a prestação será de R${:.2f}, contudo, o empréstimo foi NEGADO!".format(valor, anos, prestação))
else:
    print("Para pagar uma casa de {:.2f} em {:.2f} anos a prestação será de R${:.2f}, o empréstimo foi APROVADO!".format(valor, anos, prestação))