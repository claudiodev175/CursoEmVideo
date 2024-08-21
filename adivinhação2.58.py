from random import randint
from time import sleep
contador = 1
computador = randint(0,10)
print("Vou pensar em um número de 0 a 10, Tenta a sorte.")
sleep(2)
escolha = int(input("Qual o seu palpite? "))
while escolha != computador:
    escolha = int(input("Você errou!!, Tente novamente!!: "))
    contador += 1
if escolha == computador:
    print("Meus parabéns, Você acertou!!")
    print("Você conseguiu adivinhar em {} tentativa(s)".format(contador))
