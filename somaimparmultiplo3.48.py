n = int(input("Solicite um valor de 1 a 500: "))
soma = 0
for x in range(1,n): 
    if x % 3 == 0 and x % 2 != 0 and n <= 500:
        soma += x 
print(soma)

        
        