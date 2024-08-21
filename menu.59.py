from time import sleep
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
escolha = 0
#escolha = int(input('''[1] Somar
#[2] Multiplicar
#[3] Maior e Menor
#[4] Novos Números
#[5] Encerrar
#Qual a sua opção? '''))
while escolha != 5:
    escolha = int(input('''[1] Somar
[2] Multiplicar
[3] Maior e Menor
[4] Novos Números
[5] Encerrar
Qual a sua opção? '''))
    soma = n1 + n2
    if escolha == 1:
        print("{:.2f} + {:.2f} = {:.2f}".format(n1 , n2 , soma))
    elif escolha == 2:
        multi = n1 * n2
        print("{:.2f} X {:.2f} = {:.2f}".format(n1 , n2 , multi))
    elif escolha == 3:
        if n1 > n2:
            print("O Maior número é {:.2f}, e o menor é {:.2f}".format(n1 , n2))
        else:
            print("O Maior número é {:.2f}, e o menor é {:.2f}".format(n2 , n1))
    elif escolha == 4:
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    elif escolha == 5:
        print("Encerrando...")
        sleep(2)
    else:
        print("Opção inválida, Tente novamente!!")
        sleep(2)
        


    
