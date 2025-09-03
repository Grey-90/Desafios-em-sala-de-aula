nome = str(input("Qual seu nome?: "))
altura = float(input("Sua altura: "))
peso = float(input("Seu peso: "))

imc = peso/altura**2

print(f"Eu sou {nome} e meu imc é {imc}")