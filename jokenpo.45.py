from time import sleep
from random import choice
bot = ["Pedra","Papel","Tesoura"]
print("=" * 7)
print("JOKENPO")
print("=" * 7)
opc = int(input('''Suas opções:
[1]Pedra
[2]Papel
[3]Tesoura
'''))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
choice_bot = choice(bot)
# print(choice_bot)
if opc == 1 and choice_bot == "Pedra":
    print("Pedra vs Pedra(EMPATE!!)") 
elif opc == 1 and choice_bot == "Papel":
    print("Pedra vs Papel (DERROTA!!)")
elif opc == 1 and choice_bot == "Tesoura":
    print("Pedra vs Tesoura (VITÓRIA!!)")
elif opc == 2 and choice_bot == "Pedra":
    print("Papel vs Pedra (VITÓRIA!!)")
elif opc == 2 and choice_bot == "Papel":
    print("Papel vs Papel (EMPATE!!)")
elif opc == 2 and choice_bot == "Tesoura":
    print("Papel vs Tesoura (DERROTA!!)")
elif opc == 3 and choice_bot == "Pedra":
    print("Tesoura vs Pedra (DERROTA!!)")
elif opc == 3 and choice_bot == "Papel":
    print("Tesoura vs Papel (VITÓRIA!!)")
elif opc == 3 and choice_bot == "Tesoura":
    print("Tesoura vs Tesoura (EMPATE!!)")
elif opc != 1 and opc != 2 and opc != 3:
    print("Jogada Inválida")
