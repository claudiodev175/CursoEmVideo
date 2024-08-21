from random import randint
from time import sleep
print("=-"*20)
print("PAR OU IMPAR")
contador = 0
soma = 0
computador = 0
while True:
    print("=-"*20)
    n = int(input("Diga um valor: "))
    print("=-"*20)
    escolha = str(input("P/I: ")).upper().strip()[0]
    computador = randint(1,10)
    soma = n + computador
    resultado = soma % 2
    print(f"O Computador escolheu {computador}")
    if n > 10 or n < 0:
        print("=-"*20)
        print("Valor inválido,Digite novamente")
        sleep(2)
    if escolha in "P" and resultado == 0:
        print("Vitória")
        contador += 1
    elif escolha in "P" and resultado != 0:
        print("Derrota")
        break
    elif escolha in "I" and resultado != 0:
        print("Vitória")
        contador += 1
    elif escolha in "I" and resultado == 0:
        print("Derrota")
        break
print(f"GAME OVER!!,Você ganhou {contador}x seguida(s)")
   
    