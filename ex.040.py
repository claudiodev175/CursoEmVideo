n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1 + n2)/ 2
if media >= 7:
   print("Parabéns, você foi aprovado!!")
elif media < 7 and media >= 3:
   print("Você está de recuperação, terá sua segunda chance")
elif media < 3:
   print("Você foi reprovado!!")
