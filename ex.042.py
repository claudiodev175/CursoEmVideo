reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1 and reta1 == reta2 == reta3:
    print("Os segmentos podem formar um triângulo equilátero")
elif reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1 and reta1 != reta2 != reta3 != reta1:
    print("Os segmentos podem formar um triângulo escaleno")
elif reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1 and reta1 == reta2 != reta3 or reta1 != reta2 == reta3 or reta2 != reta1 == reta3:
    print("Os segmentos podem formar um triângulo isósceles")
else:
    print("os segmentos não podem formar um triângulo")    