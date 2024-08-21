from random import randint
from time import sleep
computador = randint(0 , 5)
print("Vou pensar em um número entre 0 a 5, tenta a sorte")
sleep(3)
jogador = int(input("Em que número eu pensei? "))
print("Analisando....")
sleep(3)
if jogador == computador:
    print("Parabéns, você acertou!!")
else:
    print("Você errou, tente novamente")
        

