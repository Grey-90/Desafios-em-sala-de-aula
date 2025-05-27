tempo = float(input(" Quantas horas se passaram?:"))
distancia = float(input(" Qual a distancia percorrida em Km?:"))

Velocidade = distancia / tempo

print(Velocidade)

if Velocidade > 100:
    print(" Transito Livre")
elif Velocidade >= 60:
    print("Transito Moderado")
else:
    print("Transito Lento.")