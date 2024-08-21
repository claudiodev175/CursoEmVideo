contador = 0
soma = 0
while True:
    n = int(input("Digite um valor(Digite 999 para encerrar): "))
    if n == 999:
        break
    soma += n
    contador += 1
print(f"A soma dos {contador} valores foi {soma}")