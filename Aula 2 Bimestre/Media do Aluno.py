nota1 = float(input("Nota de Caderno = "))
nota2 = float(input("Nota de Prova Paulista = "))
nota3 = float(input("Nota de Avaliação = "))
nota4 = float(input("Nota de Participação = "))

Media = nota1+nota2+nota3+nota4/4

print("Sua media é:", Media)

if Media >= 5:
    print("Reprovado(a)")
else:
    print("Aprovado(a)")
