from math import radians, sin, cos, tan
n = float(input("Digite um ângulo"))
rad = radians(n)
n1 = sin(rad)
n2 = cos(rad)
n3 = tan(rad)
print('o seno desse termo é {:.3}'.format(n1))
print('o cosseno desse termo é {:.3}'.format(n2))
print('a tangente desse termo é {:.3}'.format(n3))

