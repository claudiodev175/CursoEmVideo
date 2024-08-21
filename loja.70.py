contador = 0
total = 0
menor = 0
contmenor = 0
barato = ''
print("-="*20)
print("          MERCADINHO BIG BOM")
print("-="*20)
while True:
    nome = str(input("Nome do Produto: "))
    preço = float(input("Preço: R$"))
    contmenor += 1
    total += preço
    escolha = ' '
    if preço > 1000:
        contador += 1
    if escolha in "N":
        break
    if contmenor == 1 or preço < menor:
        menor = preço
        barato = nome
    escolha = ' '
    while escolha not in "SN":
        escolha = str(input("Quer continuar[S/N]? ")).upper().strip()[0]
    if escolha in "N":
        break
print(f"O Total da compra foi de R${total}")
print(f"Temos {contador} produto(s) custando acima de R$1000.00")
print(f"o produto mais barato foi {barato} que custou R${menor}")
    