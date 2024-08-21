s = str(input("Digite seu sexo:[M/F] ")).strip().upper()[0]
while(s != "M" and s != "F"):
    s = str(input("Dados inválidos, por favor, informe seu sexo: ")).strip().upper()[0]
if s in "M":
    print("O Gênero escolhido foi: Masculino")
else:
    print("O Gênero escolhido foi: Feminino")