num = int(input("Digite um número inteiro qualquer: "))
escolha = int(input("Escolha a base de conversão\n[1]Para binário\n[2]Para octal\n[3]Para hexadecimal"))
if escolha == 1:
    print("{} convertido para binário é {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertido para octal é {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("{} convertido para hexadecimal é {}".format(num, hex(num)[2:]))
else:
    print("opção inválida, tente novamente")