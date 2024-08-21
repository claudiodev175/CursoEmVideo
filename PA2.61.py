n = int(input("Digite o primeiro termo: "))
r = int(input("Diga a razão: "))
termo = n
contador = 1
while contador <= 10:
    print("{}->".format(termo), end='')
    termo += r
    contador += 1
print("FIM")
