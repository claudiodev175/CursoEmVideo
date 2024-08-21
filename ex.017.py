from math import hypot
n1 = float(input("Digite o comprimento do cateto oposto"))
n2 = float(input('Digite o comprimento do cateto adjacente'))
print('A medida da hipotenusa é {:.2f}'.format(hypot(n1 , n2)))
