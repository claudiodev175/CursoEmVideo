from time import sleep
print("Boa tarde, para viagens abaixo de 200 km é cobrado R$0,50, já para viagens acima é cobrado R$0,45")
sleep(3)
km = int(input("Qual a distância da sua viagem? "))
if km <= 200:
    print("A sua viagem vai lhe custar R${}".format(km * 0.50))
else:
    print("A sua viagem vai lhe custar R${}".format(km * 0.45))
        
