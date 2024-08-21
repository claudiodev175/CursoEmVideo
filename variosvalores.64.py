soma = 0
n = 0
contador = 0
n = int(input("Digite um número[aperte 999 para parar]: "))
while n != 999:
    #n = int(input("Digite um número[aperte 999 para parar]: "))
    soma += n
    contador += 1
    n = int(input("Digite um número[aperte 999 para parar]: "))
#print("A soma de todos os valores é {} e foram digitados {} valores".format(soma - 999,contador-1))
print("A soma de todos os valores é {} e foram digitados {} valores".format(soma - 999,contador-1))