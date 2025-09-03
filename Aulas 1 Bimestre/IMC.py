peso = float(input("Digite seu peso: "))
Altura = float(input("Digite sua altura: "))

imc = peso/(Altura * Altura)

print("Seu IMC é: ",imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
