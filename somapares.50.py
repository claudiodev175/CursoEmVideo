soma = 0
for c in range(1,7):
    num = int(input("Digite seis números pares: "))
    if num % 2 == 0:
        soma += num
    else:
        print("Valor inválido")
print(soma)
