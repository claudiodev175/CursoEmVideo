n1 = int(input("Digite o primeiro termo: "))
r = int(input("Diga a razão: "))
decimo = n1 + (10 - 1) * r
for i in range(n1,decimo + r,r):
    print(i)
print("Acabou")

