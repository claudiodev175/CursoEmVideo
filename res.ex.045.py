from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print("JOKENPO")
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print("Empate!!")
    elif jogador == 1:
        print("O Jogador vence")    
    elif jogador == 2:
        print("O Computador venceu")
elif computador == 1:
    if jogador == 0:
        print("O Computador Venceu")
    elif jogador == 1:
        print("Empate!!")
    elif jogador == 2:
        print("O Jogador venceu!!")
elif computador == 2:
    if jogador == 0:
        print("O Jogador venceu!!")
    elif jogador == 1:
        print("O Computador venceu")
    elif jogador == 2:
        print("Empate!!")
else:
    print("Jogada inválida")