print("-="*20)
print("          CALCULADORA DE IMC")
print("-="*20)
peso = float(input("Digite o seu peso: "))
print("-="*20)
altura = float(input("Digite a sua altura: "))
print("-="*20)
imc = peso/altura ** 2
print("O seu IMC é {:.2f}".format(imc))
print("-="*20)
if imc < 18.5:
    print("Você está abaixo do peso normal")
    print("-="*20)
elif imc >= 18.6 and imc <= 24.9:
    print("Você está no peso ideal, parabéns!!") 
    print("-="*20)
elif imc >= 25 and imc <= 29.9:
    print("Você está levemente acima do peso")
    print("-="*20)
elif imc >= 30 and imc <= 34.9:
    print("Você está no primeiro grau de obesidade!!")
    print("-="*20)
elif imc >= 35 and imc <= 39.9:
    print("Você possui obesidade severa")
    print("-="*20)
elif imc >= 40:
    print("Você possui obesidade mórbida")
    print("-="*20)