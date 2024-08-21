n1 = int(input("Digite um número para calcularmos o seu fatorial: "))
contador = n1
f = 1
print("Calculando {}!".format(n1, end=''))
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print("{}".format(f))