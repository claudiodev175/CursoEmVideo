preço = float(input("Valor das compras: R$"))
escolha = int(input('''Forma de pagamento:
[1] á vista no dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual a opção?'''))
if escolha == 1:
    print("O valor do produto ficará R${:.2f}".format(preço - preço * 0.1))
elif escolha == 2:
    print("O valor do produto será de R${:.2f}".format(preço - preço * 0.05))
elif escolha == 3:
    print("O valor da parcela do produto será de R${:.2f}".format(preço/2))
elif escolha == 4:
    total = preço + preço * 0.20
    totparcelas = int(input("Quantas vezes?"))
    parcela = total / totparcelas
    print("a parcela do valor será de R${:.2f}".format((parcela)))

