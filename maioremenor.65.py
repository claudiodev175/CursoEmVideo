opc = "S"
contador = 0
soma = 0
maior = 0
menor = 0
while opc in "S":
    n = int(input("Digite um valor: "))
    #opc = str(input("Quer continuar? [S/N] ")).strip().upper()
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opc = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
media = soma/contador
print("Foram {} valore(s) digitado(s) e sua média é {}".format(contador,media))
print("O Maior valor digitado foi {} e o menor foi {}".format(maior,menor))   