reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print("Os segmentos podem formar um triângulo")
else:
    print("os segmentos não podem formar um triângulo")    